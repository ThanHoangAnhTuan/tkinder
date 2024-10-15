import tkinter as tk


class Graph:
    def __init__(self, root_tk):
        self.root = root_tk
        self.root.title("Graph management application")
        self.root.state('zoomed')
        self.screen_height = self.root.winfo_screenheight()
        self.screen_width = self.root.winfo_screenwidth()
        self.button_style = {
            "font": ("Arial", 12, "bold"),  # Font chữ cho nút
            "bg": "white",  # Màu nền xanh lá cây
            "fg": "#4A90E2",  # Màu chữ trắng
            "activebackground": "white",  # Màu nền khi nhấn
            "activeforeground": "#4A90E2",  # Màu chữ khi nhấn
            "bd": 1,  # Viền nút
            "relief": "raised",  # Hiệu ứng nổi lên
            "width": 20,  # Độ rộng của nút
            "height": 2  # Độ cao của nút
        }
        self.right_frame = None
        self.left_frame = None
        self.buttons = None
        self.left_layout()
        self.right_layout()

        self.pages = {}
        self.create_pages()
        self.show_page("Shortest Path")

    def left_layout(self):
        self.left_frame = tk.Frame(self.root, width=self.screen_width * 0.2,
                                   height=self.screen_height, bg="lightblue")
        self.left_frame.pack(side="left", fill=tk.BOTH, expand=True)
        self.create_menu()

    def right_layout(self):
        self.right_frame = tk.Frame(self.root, width=self.screen_width * 0.8,
                                    height=self.screen_height)
        self.right_frame.pack(side="right", fill=tk.BOTH, expand=True)
        self.right_frame.pack_propagate(False)

    def create_menu(self):
        label = tk.Label(self.left_frame, text="Menu", bg="lightblue",
                         font=("Arial", 16, "bold"))
        label.pack(pady=10)

        # Tạo các nút bấm
        button1 = tk.Button(self.left_frame, text="Shortest Path",
                            **self.button_style,
                            command=lambda: self.show_page("Shortest Path"))
        button1.pack(pady=5)  # Khoảng cách giữa các nút là 5 pixels

        button2 = tk.Button(self.left_frame, text="Minimum Spanning Tree",
                            **self.button_style,
                            command=lambda: self.show_page(
                                "Minimum Spanning Tree"))
        button2.pack(pady=5)

        button3 = tk.Button(self.left_frame, text="Import", **self.button_style,
                            command=lambda: self.import_graph)
        button3.pack(pady=5)

        button4 = tk.Button(self.left_frame, text="Export", **self.button_style,
                            command=lambda: self.import_graph)
        button4.pack(pady=5)

        self.buttons = [button1, button2, button3, button4]

    def create_pages(self):
        for page in ["Shortest Path", "Minimum Spanning Tree"]:
            frame = tk.Frame(self.right_frame)
            self.layout_right_frame(frame, page)
            self.pages[page] = frame

    def layout_right_frame(self, frame, page):
        label = tk.Label(frame, text=f"This is the {page} page",
                         font=("Arial", 24))
        label.pack(pady=20)

    def show_page(self, page_name):
        for frame in self.pages.values():
            frame.pack_forget()
        self.pages[page_name].pack(fill=tk.BOTH, expand=True)

        for button in self.buttons:
            button.config(bg="white", fg="#4A90E2")

        active_button = self.buttons[
            ["Shortest Path", "Minimum Spanning Tree"].index(page_name)]
        # Đổi màu nút đang hoạt động
        active_button.config(bg="#4A90E2", fg="white")

    def parse_input(self):
        print("Parsing input")

    def draw_graph(self):
        print("drawing graph")

    def random_graph(self):
        print("creating random graph")

    def shortest_path(self):
        print("finding shortest path")

    def minimum_spanning_tree(self):
        print("finding minimum spanning tree")


if __name__ == "__main__":
    root_tk = tk.Tk()
    app = Graph(root_tk)
    root_tk.mainloop()
