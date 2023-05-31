import pygame


class Paint:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.colors = {'black': (0, 0, 0), 'red': (255, 0, 0), 'blue': (0, 0, 255), 'green': (0, 255, 0),
                       'yellow': (255, 255, 0)}
        self.current_color = 'black'
        self.pixel_size = 1
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        self.history = []

    def about(self):
        print('Paint Program')
        print('Developer: John Doe')
        print('Supported commands:')
        print('- About, help')
        print('- color')
        print('- linea(A, B)')
        print('- undo')
        print('- pixelSize')
        print('- draw (cuadrado, rectangulo, circle)')
        print('- draw triangulo (equilatero, escaleno, isosceles)')
        print('- background COLOR')

    def color(self, command):
        if command == 'ls':
            print('Available colors:', list(self.colors.keys()))
        elif command.startswith('set'):
            color = command.split(' ')[1]
            if color in self.colors:
                self.current_color = color
                print('Color changed to', color)
            else:
                print('Invalid color')
        else:
            print('Invalid command')

    def linea(self, point_a, point_b):
        print('Drawing line from', point_a, 'to', point_b)
        pygame.draw.line(self.surface, self.colors[self.current_color], point_a, point_b, self.pixel_size)
        self.history.append(('linea', (point_a, point_b)))

    def undo(self):
        if self.history:
            last_action = self.history.pop()
            if last_action[0] == 'linea':
                self.surface.fill((255, 255, 255))
                for action in self.history:
                    if action[0] == 'linea':
                        pygame.draw.line(self.surface, self.colors[self.current_color], *action[1], self.pixel_size)
            print('Undoing last action:', last_action[0])
            pygame.display.flip()
        else:
            print('Nothing to undo')

    def pixelSize(self, size):
        self.pixel_size = size
        print('Pixel size set to', size)

    def draw(self, shape, x, y):
        if shape == 'cuadrado':
            side_length = 100
            top_left = (x, y)
            bottom_right = (x + side_length, y + side_length)
            print('Drawing cuadrado at position (', x, ',', y, ')')
            pygame.draw.rect(self.surface, self.colors[self.current_color], (top_left, (side_length, side_length)))
            self.history.append(('cuadrado', (top_left, bottom_right)))
        elif shape == 'circle':
            radius = 50
            center = (x + radius, y + radius)
            print('Drawing circle at position (', x, ',', y, ')')
            pygame.draw.circle(self.surface, self.colors[self.current_color], center, radius)
            self.history.append(('circle', (center, radius)))
        else:
            print('Invalid shape')

    def draw_triangulo(self, type, x, y):
        print('Drawing', type, 'triangulo at position (', x, ',', y, ')')
        # Implementar la lógica para dibujar el tipo de triangulo especificado

    def background(self, color):
        print('Changing background color to', color)
        self.surface.fill(self.colors[color])
        pygame.display.flip()


def main():
    paint = Paint()
    while True:
        command = input('Enter a command: ')
        if command.lower() in ['about', 'help']:
            paint.about()
        elif command.lower().startswith('color'):
            paint.color(command.lower().replace('color', '').strip())
        elif command.lower().startswith('linea'):
            points = command[6:-1].split('),(')
            point_a = tuple(map(int, points[0].split(',')))
            point_b = tuple(map(int, points[1].split(',')))
            paint.linea(point_a, point_b)
            paint.screen.blit(paint.surface, (0, 0))
            pygame.display.flip()
        elif command.lower() == 'undo':
            paint.undo()
            paint.screen.blit(paint.surface, (0, 0))
            pygame.display.flip()
        elif command.lower().startswith('pixelsize'):
            size = int(command.lower().replace('pixelsize', '').strip())
            paint.pixelSize(size)
        elif command.lower().startswith('draw'):
            args = command.lower().replace('draw', '').strip().split(' ')
            shape = args[0]
            x = int(args[1])
            y = int(args[2])
            paint.draw(shape, x, y)
            paint.screen.blit(paint.surface, (0, 0))
            pygame.display.flip()
        elif command.lower().startswith('draw triangulo'):
            args = command.lower().replace('draw triangulo', '').strip().split(' ')
            type = args[0]
            x = int(args[1])
            y = int(args[2])
            paint.draw_triangulo(type, x, y)
        elif command.lower().startswith('background'):
            color = command.lower().replace('background', '').strip()
            paint.background(color)
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
