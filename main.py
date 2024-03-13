import pygame
import pygame_gui
import pyperclip
from MatchUpGenerator import MatchUpGenerator

COLOR_BIEGE = (242, 240, 221)
COLOR_BROWN = (105, 70, 53)
WINDOW_SIZE = (1440, 810)

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("LOL Random Selector")

manager = pygame_gui.UIManager(WINDOW_SIZE, "./theme/theme.json")

playerOptions = [str(i) for i in range(2, 11, 2)]
modeOptions = ["NG", "AR"]

### UI Elements
# player label, "Total Players"
playerLabelPositionX = 50
playerLabelPositionY = 50
playerLabelWidth = 150
playerLabelHeight = 30
playerLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((playerLabelPositionX, playerLabelPositionY), (playerLabelWidth, playerLabelHeight)),
                                            text = "Total Players",
                                            manager = manager)

# mode label, "Mode"
modeLabelPositionX = 50
modeLabelPositionY = 100
modeLabelWidth = 150
modeLabelHeight = 30
modeLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((modeLabelPositionX, modeLabelPositionY), (modeLabelWidth, modeLabelHeight)),
                                        text = "Mode",
                                        manager = manager)

# player dropdown
playerDropdownPositionX = playerLabelPositionX + playerLabelWidth
playerDropdownPositionY = playerLabelPositionY
playerDropdownWidth = 200
playerDropdownHeight = 30
playerDropdown = pygame_gui.elements.UIDropDownMenu(options_list = playerOptions,
                                                    starting_option = playerOptions[0],
                                                    relative_rect = pygame.Rect((playerDropdownPositionX, playerDropdownPositionY), (playerDropdownWidth, playerDropdownHeight)),
                                                    manager = manager)

# mode dropdown
modeDropdownPositionX = modeLabelPositionX + modeLabelWidth
modeDropdownPositionY = modeLabelPositionY
modeDropdownWidth = 200
modeDropdownHeight = 30
modeDropdown = pygame_gui.elements.UIDropDownMenu(options_list = modeOptions,
                                                    starting_option = modeOptions[0],
                                                    relative_rect = pygame.Rect((modeDropdownPositionX, modeDropdownPositionY), (modeDropdownWidth, modeDropdownHeight)),
                                                    manager = manager)

# clear textbox button
clearButtonPositionX = 50
clearButtonPositionY = 150
clearButtonWidth = modeLabelWidth + modeDropdownWidth
clearButtonHeight = 30
clearButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((clearButtonPositionX, clearButtonPositionY), (clearButtonWidth, clearButtonHeight)),
                                           text = "Clear MatchUp Information",
                                           manager = manager)

# generate matchup button
generateButtonPositionX = 50
generateButtonPositionY = 200
generateButtonWidth = modeLabelWidth + modeDropdownWidth
generateButtonHeight = 30
generateButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((generateButtonPositionX, generateButtonPositionY), (generateButtonWidth, generateButtonHeight)),
                                               text = "Generate MatchUp",
                                               manager = manager)

# copy matchup button
copyButtonPositionX = 50
copyButtonPositionY = 250
copyButtonWidth = modeLabelWidth + modeDropdownWidth
copyButtonHeight = 30
copyButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((copyButtonPositionX, copyButtonPositionY), (copyButtonWidth, copyButtonHeight)),
                                               text = "Copy MatchUp Information",
                                               manager = manager)

# export matchup button
exportButtonPositionX = 50
exportButtonPositionY = 300
exportButtonWidth = modeLabelWidth + modeDropdownWidth
exportButtonHeight = 30
exportButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((exportButtonPositionX, exportButtonPositionY), (exportButtonWidth, exportButtonHeight)),
                                               text = "Export files to matchup.txt",
                                               manager = manager)

# close button
closeButtonPositionX = 50
closeButtonPositionY = WINDOW_SIZE[1] - 60
closeButtonWidth = modeLabelWidth + modeDropdownWidth
closeButtonHeight = 30
closeButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((closeButtonPositionX, closeButtonPositionY), (closeButtonWidth, closeButtonHeight)),
                                               text = "Close Application",
                                               manager = manager)

# generate textbox
padding = 30
textBoxPositionX = playerDropdownPositionX + playerDropdownWidth + padding
textBoxPositionY = playerDropdownPositionY
textBoxWidth = WINDOW_SIZE[0] - textBoxPositionX - padding
textBoxHeight = WINDOW_SIZE[1] - textBoxPositionY - padding
textBox = pygame_gui.elements.UITextEntryBox(initial_text  = "MatchUp Information Here :D",
                                       relative_rect = pygame.Rect((textBoxPositionX, textBoxPositionY), (textBoxWidth, textBoxHeight)),
                                       manager = manager)

clock = pygame.time.Clock()
isRunning = True

while isRunning:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == clearButton:
                textBox.set_text("")
            if event.ui_element == generateButton:
                player_selection = int(playerDropdown.selected_option)
                mode_selection = modeDropdown.selected_option
                matchupGenerator = MatchUpGenerator(player_selection, mode_selection)
                matchupInformation = matchupGenerator.GenerateMatchUp()
                textBox.set_text(matchupInformation)
            if event.ui_element == copyButton:
                pyperclip.copy(textBox.get_text())
            if event.ui_element == exportButton:
                with open("matchup.txt", "w") as file:
                    file.write(textBox.get_text())
            if event.ui_element == closeButton:
                isRunning = False
        manager.process_events(event)
    manager.update(time_delta)
    window.fill(COLOR_BIEGE)
    manager.draw_ui(window)
    pygame.display.flip()

pygame.quit()