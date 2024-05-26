import pygame

class Fighter():
    def __init__(self,player,x,y,flip,data,sprite_sheet,animation_steps,sound):
        self.play = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet,animation_steps)
        self.action = 0
        self.frame_index = 0
        self.action =0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y = 0
        self.running = False
        self.attacking = False
        self.attack_type = 0
        self.attack_sound = sound
        self.hit = False
        self.health = 100
        self.alive = True

    def Load_images(self,sprite_sheet,animation_steps):

        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list =[]
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x*self.size,y * self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img,(self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
    

    def move(self,screen_width,screen_height,surface,target,round_over):
        SPEED = 10
        GRAVITY =2
        dx = 0
        dy = 0
        self.running - False
        self.attack_type = 0

        key = pygame.key.get_pressed()

        if self.attacking == False and self.alive == True and round_over == False:
            if self.player ==1:
                if key[pygame.K_a]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = -SPEED
                    self.running = True
                
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.attack(target)
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
        
            if self.player ==2:
                if key[pygame.K_LEFT]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = -SPEED
                    self.running = True
                
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                if key[pygame.K_j] or key[pygame.K_k]:
                    self.attack(target)
                    if key[pygame.K_j]:
                        self.attack_type = 1
                    if key[pygame.K_k]:
                        self.attack_type = 2

           
