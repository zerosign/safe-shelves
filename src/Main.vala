using Gtk;

public struct Account {
	const String name;
	const String password;
};

public class SafeWidget : Widget {

	private Gtk.ListStore storage;
	
	public SafeWindow() {
		this.storage = new Gtk.ListStore(2, typeof(String), typeof(String));
	}
}

int main(string[] args) {
	Gtk.init(ref args);

	var window = new Window();
	window.title = "Password Safes";
	window.border_width = 10;
	window.window_position = WindowPosition.CENTER;
	window.set_default_size(500, 300);
    window.destroy.connect(Gtk.main_quit);
	window.show_all();
	
	Gtk.main();
	return 0;
}