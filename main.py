import pygame

def main():
    print("\nReading Controller Input\n")
    clock = pygame.time.Clock()
    done = False
    
    try:
        
        while not done:
            clock.tick(60)
            if pygame.joystick.get_count() > 0:
                gamepad = pygame.joystick.Joystick(0)
                gamepad.init()
            
            for event in pygame.event.get():                
                if event.type == pygame.JOYDEVICEADDED:
                    print("device added")
                
                if event.type == pygame.JOYDEVICEREMOVED:
                    print("device removed")
                    
                if event.type == pygame.JOYBUTTONDOWN:
                    button = event.dict.get("button")
                    
                    print(f"pushed button {button}")
                    
                    if button == 11:
                        done = True
                    
                # if event.type == pygame.JOYBUTTONUP:
                #     print("button released")
                    
                # if event.type == pygame.JOYAXISMOTION:
                #     print("joystick moved")
            
    except Exception:
        done = True

if __name__ == "__main__":
    pygame.init()
    pygame.joystick.init()
    main()
    pygame.quit()
