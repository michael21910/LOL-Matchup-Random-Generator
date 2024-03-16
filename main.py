import pygame
import pygame_gui
import pyperclip
from MatchUpGenerator import MatchUpGenerator

COLOR_BIEGE = (242, 240, 221)
COLOR_BROWN = (105, 70, 53)
WINDOW_SIZE = (1440, 810)
PLAYER_OPTIONS = [str(i) for i in range(1, 11)]
MODE_OPTIONS = ["NG", "AR"]
SPY_OPTIONS = ["ON", "OFF", "ONLY SPY"]
COMPONENT_X_INIT_POSITION = 50
COMPONENT_Y_INIT_POSITION = 50
COMPONENT_Y_DISTANCE = 50
LABEL_WIDTH = 150
DROPDOWN_WIDTH = 200
BUTTON_WIDTH = LABEL_WIDTH + DROPDOWN_WIDTH
LABEL_HEIGHT = DROPDOWN_HEIGHT = BUTTON_HEIGHT = 30

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("LOL Random Selector")

manager = pygame_gui.UIManager(WINDOW_SIZE, "./theme/theme.json")

### UI Elements
# player label, "Total Players"
playerLabelPositionX = COMPONENT_X_INIT_POSITION
playerLabelPositionY = COMPONENT_Y_INIT_POSITION
playerLabelWidth = LABEL_WIDTH
playerLabelHeight = LABEL_HEIGHT
playerLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((playerLabelPositionX, playerLabelPositionY), (playerLabelWidth, playerLabelHeight)),
                                            text = "Total Players",
                                            manager = manager)

# player dropdown
playerDropdownPositionX = playerLabelPositionX + playerLabelWidth
playerDropdownPositionY = playerLabelPositionY
playerDropdownWidth = DROPDOWN_WIDTH
playerDropdownHeight = DROPDOWN_HEIGHT
playerDropdown = pygame_gui.elements.UIDropDownMenu(options_list = PLAYER_OPTIONS,
                                                    starting_option = PLAYER_OPTIONS[0],
                                                    relative_rect = pygame.Rect((playerDropdownPositionX, playerDropdownPositionY), (playerDropdownWidth, playerDropdownHeight)),
                                                    manager = manager)

# mode label, "Mode"
modeLabelPositionX = COMPONENT_X_INIT_POSITION
modeLabelPositionY = playerLabelPositionY + COMPONENT_Y_DISTANCE
modeLabelWidth = LABEL_WIDTH
modeLabelHeight = LABEL_HEIGHT
modeLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((modeLabelPositionX, modeLabelPositionY), (modeLabelWidth, modeLabelHeight)),
                                        text = "Game Mode",
                                        manager = manager)


# mode dropdown
modeDropdownPositionX = modeLabelPositionX + modeLabelWidth
modeDropdownPositionY = modeLabelPositionY
modeDropdownWidth = DROPDOWN_WIDTH
modeDropdownHeight = DROPDOWN_HEIGHT
modeDropdown = pygame_gui.elements.UIDropDownMenu(options_list = MODE_OPTIONS,
                                                    starting_option = MODE_OPTIONS[0],
                                                    relative_rect = pygame.Rect((modeDropdownPositionX, modeDropdownPositionY), (modeDropdownWidth, modeDropdownHeight)),
                                                    manager = manager)

# spy mode label, "Spy Mode"
spyModeLabelPositionX = COMPONENT_X_INIT_POSITION
spyModeLabelPositionY = modeLabelPositionY + COMPONENT_Y_DISTANCE
spyModeLabelWidth = LABEL_WIDTH
spyModeLabelHeight = LABEL_HEIGHT
spyModeLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((spyModeLabelPositionX, spyModeLabelPositionY), (spyModeLabelWidth, spyModeLabelHeight)),
                                            text = "Spy Mode",
                                            manager = manager)

# spy mode dropdown
spyModeDropdownPositionX = spyModeLabelPositionX + spyModeLabelWidth
spyModeDropdownPositionY = spyModeLabelPositionY
spyModeDropdownWidth = DROPDOWN_WIDTH
spyModeDropdownHeight = DROPDOWN_HEIGHT
spyModeDropdown = pygame_gui.elements.UIDropDownMenu(options_list = SPY_OPTIONS,
                                                    starting_option = SPY_OPTIONS[0],
                                                    relative_rect = pygame.Rect((spyModeDropdownPositionX, spyModeDropdownPositionY), (spyModeDropdownWidth, spyModeDropdownHeight)),
                                                    manager = manager)

# clear textbox button
clearButtonPositionX = COMPONENT_X_INIT_POSITION
clearButtonPositionY = spyModeLabelPositionY + COMPONENT_Y_DISTANCE
clearButtonWidth = BUTTON_WIDTH
clearButtonHeight = BUTTON_HEIGHT
clearButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((clearButtonPositionX, clearButtonPositionY), (clearButtonWidth, clearButtonHeight)),
                                           text = "Clear MatchUp Information",
                                           manager = manager)

# generate matchup button
generateButtonPositionX = COMPONENT_X_INIT_POSITION
generateButtonPositionY = clearButtonPositionY + COMPONENT_Y_DISTANCE
generateButtonWidth = BUTTON_WIDTH
generateButtonHeight = BUTTON_HEIGHT
generateButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((generateButtonPositionX, generateButtonPositionY), (generateButtonWidth, generateButtonHeight)),
                                               text = "Generate MatchUp",
                                               manager = manager)

# copy matchup button
copyButtonPositionX = COMPONENT_X_INIT_POSITION
copyButtonPositionY = generateButtonPositionY + COMPONENT_Y_DISTANCE
copyButtonWidth = BUTTON_WIDTH
copyButtonHeight = BUTTON_HEIGHT
copyButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((copyButtonPositionX, copyButtonPositionY), (copyButtonWidth, copyButtonHeight)),
                                               text = "Copy MatchUp Information",
                                               manager = manager)

# export matchup button
exportButtonPositionX = COMPONENT_X_INIT_POSITION
exportButtonPositionY = copyButtonPositionY + COMPONENT_Y_DISTANCE
exportButtonWidth = BUTTON_WIDTH
exportButtonHeight = BUTTON_HEIGHT
exportButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((exportButtonPositionX, exportButtonPositionY), (exportButtonWidth, exportButtonHeight)),
                                               text = "Export files to matchup.txt",
                                               manager = manager)

# close button
# closeButtonPositionX = 50
# closeButtonPositionY = WINDOW_SIZE[1] - 60
# closeButtonWidth = modeLabelWidth + modeDropdownWidth
# closeButtonHeight = 30
# closeButton = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((closeButtonPositionX, closeButtonPositionY), (closeButtonWidth, closeButtonHeight)),
#                                                text = "Close Application",
#                                                manager = manager)

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
                totalPlayer = int(playerDropdown.selected_option)
                gameMode = modeDropdown.selected_option
                spyMode = spyModeDropdown.selected_option
                matchupGenerator = MatchUpGenerator(totalPlayer, gameMode, spyMode)
                matchupInformation = matchupGenerator.GenerateMatchUp()
                textBox.set_text(matchupInformation)
            if event.ui_element == copyButton:
                pyperclip.copy(textBox.get_text())
            if event.ui_element == exportButton:
                with open("matchup.txt", "w") as file:
                    file.write(textBox.get_text())
        if spyModeDropdown.selected_option == "ONLY SPY":
            modeDropdown.disable()
        else:
            modeDropdown.enable()
        manager.process_events(event)
    manager.update(time_delta)
    window.fill(COLOR_BIEGE)
    manager.draw_ui(window)
    pygame.display.flip()

pygame.quit()