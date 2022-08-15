# import pygame
# import pygame_menu
#
#
# class MainMenu():
#
#
#     def __init__(self, window):
#         self.menu = pygame_menu.Menu('Algorithm Visualizer', 400, 500, theme=pygame_menu.themes.THEME_ORANGE)
#         self.start = self.menu.add.button('Start', self.get_state)
#         self.selector = self.menu.add.selector('Mode :', [('Search', 1), ('Sort', 2)], )
#         self.menu.add.button('Quit', pygame_menu.events.EXIT)
#         self.menu.add.text_input('')
#         self.menu.add.text_input('')
#         self.menu.add.text_input('')
#         self.menu.add.text_input('')
#         self.menu.add.text_input('')
#         self.menu.add.text_input('Coded by Praise Eneh', copy_paste_enable=False, cursor_selection_enable=False)
#         self.menu.mainloop(window)
#
#     def get_state(self):
#         print('hello')
#         self.close()
#         pass
