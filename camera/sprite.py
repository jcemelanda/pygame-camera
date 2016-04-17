from pygame.sprite import Group


class CameraGroup(Group):
    def __init__(self, camera, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera = camera

    def draw(self, surface):
        for sprite in self.sprites():
            surface.blit(sprite.image, self.camera.apply(sprite))
