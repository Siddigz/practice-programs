
class SelectNumber:
    def __init__(self, pygame, font):
        self.pygame = pygame
        self.btn_w = 80
        self.btw_h = 80
        self.my_font = font

        self.color_selected = (0,255,0)
        self.color_normal = (200, 200, 200)

        self.btn_positions = [(950,50),(1050,50),
                              (950,150), (1050, 150),
                              (950,250), (1050, 250),
                              (950,350), (1050, 350),
                              (1050,450)            ]
        
    def draw(self, pygame, surface):
        for index, pos in enumerate(self.btn_positions):
            rect = pygame.Rect(pos[0], pos[1], self.btn_w, self.btw_h)
            pygame.draw.rect(surface, self.color_normal, rect, width=3, border_radius=10)
            
            # num_text = self.my_font.render(str(index + 1), True, (0, 0, 0))
            # text_rect = num_text.get_rect(center=rect.center)
            # surface.blit(num_text, text_rect)