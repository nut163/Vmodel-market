```python
import tkinter as tk
from royalties_system import royalties_calculation, royalties_tracking

class RoyaltiesTrackingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Royalties Tracking")
        self.create_widgets()

    def create_widgets(self):
        self.royalties_label = tk.Label(self.root, text="Royalties Earned:")
        self.royalties_label.pack()

        self.royalties_display = tk.Text(self.root, height=10, width=50)
        self.royalties_display.pack()

        self.refresh_button = tk.Button(self.root, text="Refresh", command=self.update_royalties)
        self.refresh_button.pack()

    def update_royalties(self):
        self.royalties_display.delete(1.0, tk.END)
        royalties_data = royalties_tracking.trackRoyalties()
        for data in royalties_data:
            self.royalties_display.insert(tk.END, f"Voice Model: {data['voice_model']}\n")
            self.royalties_display.insert(tk.END, f"Royalties Earned: {data['royalties_earned']}\n")
            self.royalties_display.insert(tk.END, "-----------------------------\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = RoyaltiesTrackingUI(root)
    root.mainloop()
```