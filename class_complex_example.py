"""
Rewrite of the complex example of CustomTkinter using classes
"""
import tkinter
import tkinter.messagebox
import customtkinter


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    """
    Main application class for CustomTkinter GUI
    """
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example using Classes")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = SideBar(self)
        self.sidebar_frame.configure(width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(
            row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        self.main_button_1 = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
        )
        self.main_button_1.grid(
            row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = TabviewFrame(self)
        self.tabview.configure(width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create radiobutton frame
        self.radiobutton_frame = RadioButtonFrame(self)
        self.radiobutton_frame.grid(
            row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew"
        )

        # create slider and progressbar frame
        self.slider_progressbar_frame = SliderProgressbarFrame(self)
        self.slider_progressbar_frame.configure(fg_color="transparent")
        self.slider_progressbar_frame.grid(
            row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        # create scrollable frame
        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.configure(label_text="CTkScrollableFrame")
        self.scrollable_frame.grid(
            row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # create checkbox and switch frame
        self.checkbox_slider_frame = CheckboxSwitchFrame(self)
        self.checkbox_slider_frame.grid(
            row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew"
        )

        # set default values
        self.textbox.insert(
            "0.0",
            "CTkTextbox\n\n"
            + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed \
                diam nonumy eirmod tempor invidunt ut labore et dolore magna \
                    aliquyam erat, sed diam voluptua.\n\n"
            * 20,
        )

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """
        Changes the appearence of the CustomTkinter GUI to one of three
        available modes: "System" (standard), "Dark", "Light"

        Args:
            new_appearance_mode (str): "System" (standard), "Dark", "Light"
        """
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        """
        Changes the scale of the GUI

        Args:
            new_scaling (str): string in a percentage structure 1%-100%
        """
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        """
        Sidebar button event
        """
        print("sidebar_button click")

class SideBar(customtkinter.CTkFrame):
    """
    Sidebar Frame element

    This classes uses outside functions from the controller, given as an
    additional parameter when the class is instatiated.

    This is the best structure when you have functions that might be used
    by other components built-in in the main application or as another class

    Args:
        customtkinter (_type_): CustomTkinter component
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        logo_label = customtkinter.CTkLabel(
            self,
            text="CustomTkinter",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        sidebar_button_1 = customtkinter.CTkButton(
            self, command=self.sidebar_button_event
        )
        sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        sidebar_button_2 = customtkinter.CTkButton(
            self, command=self.sidebar_button_event
        )
        sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        sidebar_button_3 = customtkinter.CTkButton(
            self, command=self.sidebar_button_event
        )
        sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        appearance_mode_label = customtkinter.CTkLabel(
            self, text="Appearance Mode:", anchor="w"
        )
        appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        scaling_label = customtkinter.CTkLabel(
            self, text="UI Scaling:", anchor="w"
        )
        scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        scaling_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # set default values
        sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        appearance_mode_optionemenu.set("Dark")
        scaling_optionemenu.set("100%")
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        """
        Changes the appearence of the CustomTkinter GUI to one of three
        available modes: "System" (standard), "Dark", "Light"

        Args:
            new_appearance_mode (str): "System" (standard), "Dark", "Light"
        """
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        """
        Changes the scale of the GUI

        Args:
            new_scaling (str): string in a percentage structure 1%-100%
        """
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        """
        Sidebar button event
        """
        print("sidebar_button click")


class RadioButtonFrame(customtkinter.CTkFrame):
    """
    Radio Button frame with no functions

    Args:
        customtkinter (_type_): CustomTkinter component
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(
            master=self, text="CTkRadioButton Group:"
        )
        self.label_radio_group.grid(
            row=0, column=2, columnspan=1, padx=10, pady=10, sticky=""
        )
        self.radio_button_1 = customtkinter.CTkRadioButton(
            master=self, variable=self.radio_var, value=0
        )
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(
            master=self, variable=self.radio_var, value=1
        )
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(
            master=self, variable=self.radio_var, value=2
        )
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # set default values
        self.radio_button_3.configure(state="disabled")


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    """
    Scrollable Frame class for CustomTkinter
    
    Args:
        customtkinter (_type_): CustomTkinter component
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(
                master=self, text=f"CTkSwitch {i}"
            )
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            scrollable_frame_switches.append(switch)

        # set default values
        scrollable_frame_switches[0].select()
        scrollable_frame_switches[4].select()


class CheckboxSwitchFrame(customtkinter.CTkFrame):
    """
    CustomTkinter Frame class

    Args:
        customtkinter (_type_): CustomTkinter component
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        checkbox_1 = customtkinter.CTkCheckBox(master=self)
        checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        checkbox_2 = customtkinter.CTkCheckBox(master=self)
        checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        checkbox_3 = customtkinter.CTkCheckBox(master=self)
        checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        checkbox_3.configure(state="disabled")
        checkbox_1.select()


class SliderProgressbarFrame(customtkinter.CTkFrame):
    """
    CustomTkinter Frame class

    Args:
        customtkinter (_type_): CustomTkinter component
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        seg_button_1 = customtkinter.CTkSegmentedButton(
            self
        )
        seg_button_1.grid(
            row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew"
        )
        progressbar_1 = customtkinter.CTkProgressBar(self)
        progressbar_1.grid(
            row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew"
        )
        progressbar_2 = customtkinter.CTkProgressBar(self)
        progressbar_2.grid(
            row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew"
        )
        slider_1 = customtkinter.CTkSlider(
            self, from_=0, to=1, number_of_steps=4
        )
        slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        slider_2 = customtkinter.CTkSlider(
            self, orientation="vertical"
        )
        slider_2.grid(
            row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns"
        )
        progressbar_3 = customtkinter.CTkProgressBar(
            self, orientation="vertical"
        )
        progressbar_3.grid(
            row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns"
        )

        # set default values
        slider_1.configure(command=progressbar_2.set)
        slider_2.configure(command=progressbar_3.set)
        progressbar_1.configure(mode="indeterminnate")
        progressbar_1.start()
        seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        seg_button_1.set("Value 2")


class TabviewFrame(customtkinter.CTkTabview):
    """
    CustomTkinter Tabview class

    This classes uses functions that are independent from the controller,
    and doesn't need the controller to be given as an additional parameter
    when the class is instatiated.

    * bind and unbind functions implemented do avoid the W0223 pylint error

    Args:
        customtkinter (_type_): CustomTkinter component
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add("CTkTabview")
        self.add("Tab 2")
        self.add("Tab 3")
        self.tab("CTkTabview").grid_columnconfigure(
            0, weight=1
        )  # configure grid of individual tabs
        self.tab("Tab 2").grid_columnconfigure(0, weight=1)

        optionmenu_1 = customtkinter.CTkOptionMenu(
            self.tab("CTkTabview"),
            dynamic_resizing=False,
            values=["Value 1", "Value 2", "Value Long Long Long"],
        )
        optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        combobox_1 = customtkinter.CTkComboBox(
            self.tab("CTkTabview"),
            values=["Value 1", "Value 2", "Value Long....."],
        )
        combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        string_input_button = customtkinter.CTkButton(
            self.tab("CTkTabview"),
            text="Open CTkInputDialog",
            command=self.open_input_dialog_event,
        )
        string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        label_tab_2 = customtkinter.CTkLabel(
            self.tab("Tab 2"), text="CTkLabel on Tab 2"
        )
        label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # set default values
        optionmenu_1.set("CTkOptionmenu")
        combobox_1.set("CTkComboBox")

    def bind(self, sequence = None, command = None, add = None):
        pass

    def unbind(self, sequence: str | None = None, funcid: str | None = None ):
        pass

    def open_input_dialog_event(self):
        """Input dialog button event
        """
        dialog = customtkinter.CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog"
        )
        print("CTkInputDialog:", dialog.get_input())

if __name__ == "__main__":
    app = App()
    app.mainloop()
