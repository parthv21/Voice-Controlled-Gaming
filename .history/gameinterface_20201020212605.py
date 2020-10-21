class GameInterface:
    
    def __init__(self):
        super().__init__()
        self.command1 = None
        self.command0 = None
    # Text based command

    def processCommand(self, command):
        if command != "silence":     
            if command == "left":
                if self.command1 == "go":
                    # Keep going left
                    pass
                    
            # Command 0 is second last command 
            # Command 1 is last command
            self.command0 = self.command1
            self.command1 = command

