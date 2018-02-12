#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

import pygame
import time
import random
import sys
import math

#### ====================================================================================================================== ####
#############                                         INITIALIZE                                                   #############
#### ====================================================================================================================== ####

def initialize():
    ''' Central Initialize function. Calls helper functions to initialize Pygame and then the gameData dictionary.
    Input: None
    Output: gameData Dictionary
    '''
    screen = initializePyGame()
    return initializeData(screen)

#############                                           HELPERS                                                    #############
#### ---------------------------------------------------------------------------------------------------------------------- ####

def initializeData(screen, numCannonBalls=6, numTargets=1):   #############IMPORTANT
    ''' Initializes the gameData dictionary. Includes: Entity Data and Logistical Data (isOpen).
    Input: pygame screen
    Output: gameData Dictionary
    '''
    # Initialize gameData Dictionary
    gameData = {"screen": screen,
                "background": pygame.transform.scale(pygame.image.load("resources/backgrounds/background.png").convert_alpha(), (1200, 800)),
                "OVER":pygame.transform.scale(pygame.image.load("resources/rank.png").convert_alpha(), (1200, 800)),
                "entities": [],
                'isOpen': True,
                "ammo": pygame.transform.scale(pygame.image.load("resources/cannonball/cannonball.png").convert_alpha(), (20,20)),    
                "settings": {"maxTargets": numTargets,
                             "maxCannonBalls": numCannonBalls},
                "score":0,
                'gameover':False}

    # Initialize Target Object(s)
    for _ in range(numTargets):
        gameData["entities"].append({"type": "target",
                                     "location": [random.randint(100, 400), random.randint(200, 600)],
                                     "size": (150, 150),
                                     "sprite": pygame.transform.scale(pygame.image.load("resources/targets/target_{}.png".format(random.randint(1, 4))).convert_alpha(), (150, 150)),
                                     "isHit": False,
                                     "isDisappear": False,
                                     "clock": 0
                                     })

    # Initialize CannonBall Object(s)
    for _ in range(numCannonBalls):
        gameData["entities"].append({"type": "cannonball",
                                     "location": [1100, 750],
                                     "velocity": None,
                                     "size": (25,25),
                                     "sprite": pygame.transform.scale(pygame.image.load("resources/cannonball/cannonball.png").convert_alpha(), (25,25)),
                                     "exists": False,
                                     "destroy": False,
                                     "reload":False})


    # Initialize Cannon Object(s)
    gameData["entities"].append({"type": "cannon",
                                 "location": [1100, 550], # Note: When rotating, you may need to adjust the location to (1300, 875) depending on your method
                                 "size": (200, 150),
                                 "sprite": pygame.transform.scale(pygame.image.load("resources/cannons/cannon_{}.png".format(random.randint(1, 4))).convert_alpha(), (200, 150)),
                                 "loaded": True,
                                 "isFiring": False,
                                 "angle": 45.00,
                                 "isMoving": False,
                                 "power": 10,
                                 "velocity": [0,10]
                                 })

    # Initialize CrossHair Object
    gameData["entities"].append({"type": "crosshair",
                                 "location": pygame.mouse.get_pos(),
                                 "size": (100, 100),
                                 "hasMoved": False,
                                 "sprite": pygame.transform.scale(pygame.image.load("resources/crosshairs/crosshair_{}.png".format(random.randint(1, 4))).convert_alpha(), (100, 100))})
    
    return gameData

def initializePyGame():
    ''' Initializes Pygame.
    Input: None
    Output: pygame screen
    '''
    pygame.init()
    pygame.key.set_repeat(1, 1)
    return pygame.display.set_mode((1200, 800))

#### ====================================================================================================================== ####
#############                                           PROCESS                                                    #############
#### ====================================================================================================================== ####

def process(gameData):
    ''' Central Process function. Calls helper functions to handle various KEYDOWN events.
    Input: gameData Dictionary
    Output: None
    '''
    # Handle Game over or not
    Over=True
    for entity in gameData["entities"]:
        if entity['type']== "cannonball":
            if entity['destroy']==False:
                Over=False
                break
     

    
    events = pygame.event.get()
    for event in events:
        
        # Handle [x] Press
        if event.type == pygame.QUIT:
            gameData['isOpen'] = False
            
        # Handle Key Presses
        if event.type == pygame.KEYDOWN:
                
            # Handle 'Escape' Key
            if event.key == pygame.K_ESCAPE:
                handleKeyEscape(gameData)

        # Handle Mouse Movement
        if event.type == pygame.MOUSEMOTION:
            handleMouseMovement(gameData)

        # Handle Mouse Click
        if event.type == pygame.MOUSEBUTTONUP:
            handleMouseClick(gameData)
    if Over== True:
        gameData['gameover']=True


#############                                           HANDLERS                                                   #############
#### ---------------------------------------------------------------------------------------------------------------------- ####

def handleMouseMovement(gameData):
    ''' Replace this and the return statement with your code '''
    for entity in gameData['entities']:
        if  entity['type']=="cannon":
            entity["isMoving"]= True
        if  entity['type']=="crosshair":
            entity["hasMoved"]= True
    return
        
def handleMouseClick(gameData):   #now
    ''' Replace this and the return statement with your code '''
    for entity in gameData["entities"]:
        if entity['type']== "cannonball":
            if entity['exists']==False:
                entity['exists']=True
                break
    return

def handleKeyEscape(gameData):
    ''' Handles the Escape KEYDOWN event. Sets a flag for 'isOpen' to 'False'.
    Input: gameData Dictionary
    Output: None
    '''
    gameData['isOpen'] = False

#### ====================================================================================================================== ####
#############                                            UPDATE                                                    #############
#### ====================================================================================================================== ####
    
def update(gameData):
    ''' Central Update function. Calls helper functions to update various types of Entities [crosshair, target, cannon, cannonball].
    Input: gameData Dictionary
    Output: None
    '''
    for entity in gameData["entities"]:
        if entity['type'] == 'crosshair' and entity['hasMoved'] == True:
            updateCrossHair(entity)
        if entity['type'] == 'cannon' :
            updateCannon(entity)
        if entity['type'] == 'cannonball' and entity['exists'] == True:
            cannonEntity = None
            targetEntity = None
            for moreEntities in gameData["entities"]:
                if moreEntities["type"] == "target":
                    targetEntity = moreEntities
                elif moreEntities["type"] == "cannon":
                    cannonEntity = moreEntities
            updateCannonBall(entity, cannonEntity, targetEntity)
        if entity['type'] == 'target':# and entity['isHit'] == True:
            if entity['isHit'] == True:
                gameData["score"]+=1
            updateTarget(entity)

            

#############                                           HELPERS                                                    #############
#### ---------------------------------------------------------------------------------------------------------------------- ####

def updateCrossHair(entity):
    ''' Replace this and the return statement with your code '''
    if  entity['type']=="crosshair":
        if entity["hasMoved"]== True:
            (mousex,mousey)=pygame.mouse.get_pos()
            entity["location"]=[mousex,mousey]
    return

def updateCannon(entity):
    ''' Replace this and the return statement with your code '''
    if  entity['type']=="cannon":
        if entity["isMoving"]== True:
            (mousex,mousey)=pygame.mouse.get_pos()
            #entity["angle"] = - (math.atan2(825- mousey, 1300 - mousex)) * 180/math.pi + 270
            #entity["angle"] = - (math.atan2(entity['location'][1]+int(0.5*entity['size'][1])- mousey, entity['location'][0]+int(0.5*entity['size'][0]) - mousex)) * 180/math.pi + 270
            entity["angle"] = - (math.atan2(entity['location'][1] - mousey, entity['location'][0] - mousex)) * 180/math.pi + 270
        entity["location"][0]+=entity["velocity"][0]
        entity["location"][1]+=entity["velocity"][1]        
        if entity["location"][1]>=750 or entity["location"][1]<=50:
            entity["velocity"][1]=-entity["velocity"][1]
    return

def updateCannonBall(entity, cannonEntity, targetEntity):  #now
    ''' Replace this and the return statement with your code '''

    if entity['type']== "cannonball":
        if entity['destroy']==True:
            entity['location']=cannonEntity['location']
            entity['velocity']=None
            entity['reload']= False
        if entity['reload']==True:
            entity['location']=cannonEntity['location']
            entity['velocity']=None
            entity['destroy']= False
            entity['exists']= False
            entity['reload']= False
        if entity['velocity']==None:
            (mousex,mousey)=pygame.mouse.get_pos()
            entity['location']=[cannonEntity['location'][0],cannonEntity['location'][1]]
            angle= math.atan2(entity['location'][1]- mousey, entity['location'][0] - mousex)
            entity['velocity']=[-15*math.cos(angle),-15*math.sin(angle)]
        else :
            if entity['location'][0]>1200 or entity['location'][1]>800 or  entity['location'][0]<0 or entity['location'][1]<0:
                entity['destroy']=True
            elif (entity['location'][0]+int(0.5*entity['size'][0])-targetEntity['location'][0]- int(0.5*targetEntity['size'][0]))**2+(entity['location'][1]+int(0.5*entity['size'][1])-targetEntity['location'][1]- int(0.5*targetEntity['size'][1]))**2<=(int(0.5*entity['size'][1])+int(0.5*targetEntity['size'][1]))**2:
                targetEntity['isHit']=True
                entity['reload']=True
            else:
                entity['velocity'][1]+=0.03
                entity['location'][0]+=entity['velocity'][0]
                entity['location'][1]+=entity['velocity'][1]
    return


def updateTarget(entity):
    ''' Replace this and the return statement with your code '''
    if entity['type']== "target":
        clocktar = pygame.time.Clock()
        if  entity['isHit']==True:
            entity['location']=[random.randint(100, 400), random.randint(200, 600)]
            entity['sprite']=pygame.transform.scale(pygame.image.load("resources/targets/target_{}.png".format(random.randint(1, 4))).convert_alpha(), (150, 150))
            entity['isHit']=False
            entity['isDisappear']=False
            entity['clock']=0
        elif entity['isDisappear']==True:
            entity['location']=[random.randint(100, 400), random.randint(200, 600)]
            entity['sprite']=pygame.transform.scale(pygame.image.load("resources/targets/target_{}.png".format(random.randint(1, 4))).convert_alpha(), (150, 150))
            entity['isHit']=False
            entity['isDisappear']=False
            entity['clock']=0
        else:
            if entity['clock']>=400:
                entity['isDisappear']=True            
            else:
                clocktar.tick(400)
                entity['clock']+=clocktar.get_time()
                print(entity['clock'])
    return

#### ====================================================================================================================== ####
#############                                            RENDER                                                    #############
#### ====================================================================================================================== ####

def render(gameData):
    ''' Central Render function. Calls helper functions to render various views.
    Input: gameData Dictionary
    Output: None
    '''
    gameData["screen"].blit(gameData["background"], (0, 0))
    ammo=[]
    for entity in gameData["entities"]:
        if entity['type'] == 'cannon':
            renderCannon(gameData, entity)
        elif entity['type'] == 'cannonball':
            renderCannonBall(gameData, entity)
            if entity['exists'] ==True :
                ammo.append(entity)             
        elif entity['type'] == 'target':
            renderTarget(gameData, entity)
        elif entity['type'] == 'crosshair':
            renderCrossHair(gameData, entity)
    renderAmmo(gameData, ammo)
    pygame.display.flip()

def renderscore(gameData):
    scorefont=pygame.font.Font(None,30)
    #get the color of the entity
    colorinfo=(250,100,0)
    #draw the name of socre	
    scoretext=scorefont.render("Game Score= {}".format(gameData['score']),1,colorinfo)
    gameData["screen"].blit(scoretext, (1000, 50))
    pygame.display.update()
    

#############                                           HELPERS                                                    #############
#### ---------------------------------------------------------------------------------------------------------------------- ####

def renderTarget(gameData, entity):
    ''' Replace this and the return statement with your code '''
    if entity['type']== "target":
        gameData["screen"].blit(entity["sprite"],entity["location"])
    return


def renderCrossHair(gameData, entity):
    ''' Replace this and the return statement with your code '''
    if entity['type']== "crosshair":
        gameData["screen"].blit(entity["sprite"],[entity["location"][0]-50,entity["location"][1]-50])
    return

def renderCannon(gameData, entity):   
    ''' Replace this and the return statement with your code '''
    rotated_image = pygame.transform.rotate(entity["sprite"], entity['angle'])
    new_size=rotated_image.get_size()
    newx=entity["location"][0]-int(0.5*new_size[0])
    newy=entity["location"][1]-int(0.5*new_size[1])
    gameData["screen"].blit(rotated_image ,[newx,newy])
    return

def renderCannonBall(gameData, entity):  
    ''' Replace this and the return statement with your code ''' 
    if entity['type']== "cannonball":
        if entity['exists']==True:
            gameData["screen"].blit(entity["sprite"],entity["location"])
    return

def renderAmmo(gameData, ammoList):
    ''' Replace this and the return statement with your code '''
    for i in range(6-len(ammoList)):
        gameData["screen"].blit(gameData["ammo"],[100+i*40,700])
    return
def renderGameOver(gameData):
    ''' Replace this and the return statement with your code '''
    if gameData['gameover']== True:
        gameData["screen"].blit(gameData["OVER"],(0,0))
        scorefont=pygame.font.Font(None,66)
        overfont=pygame.font.Font(None,100)
        Scolor=(250,188,100)
        Ocolor=(250,10,0)
        #draw the name of socre	
        scoretext=scorefont.render("Your Score: {}".format(gameData['score']),1,Scolor)
        overtext=overfont.render("GAME OVER",1,Ocolor)
        gameData["screen"].blit(scoretext, (450, 420))
        gameData["screen"].blit(overtext, (400,200 ))
        pygame.display.update()
    
    return

#### ====================================================================================================================== ####
#############                                             MAIN                                                     #############
#### ====================================================================================================================== ####

def main():
    ''' Main function of script - calls all central functions above via a Game Loop code structure.
    Input: None
    Output: None
    '''
    # Initialize Data and Pygame
    gameData = initialize()
    
    # Begin Central Game Loop
    while gameData['isOpen']:
        process(gameData)
        update(gameData)
        if gameData['gameover']== False:
            render(gameData)
            renderscore(gameData)
        else:
            renderGameOver(gameData)
        time.sleep(0.01) # Small Time delay to slow down frames per second
        
    # Exit Pygame and Python
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
