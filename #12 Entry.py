#!/usr/bin/python3

# Gtk.Entry
# 	-	set_text(str)
# 	-	get_text() return str
# 	-	set_max_length()
# 	-	set_editable(Boolean)
#	-	set_alignment(float(0-1))
# 	-	set_visibility(Boolean)
# 	-	set_progress_fraction(float(0-1))
# 	-	set_progress_pulse_step(float(0-1))
#		- GLib
#			- timeout_add(100, function, user data)
#			- source_remove(object)
# 	-	progress_pulse()
# 	-	set_icon_from_icon_name(Enum, Icon name)
# 	-	set_icon_tooltip_text()
#		-	Gtk.EntryIconPosition
#			-	PRIMARY		0
#			-	SECONDARY	1

# Signals
# 	-	activate
# 	-	backspace
# 	-	copy-clipboard
# 	-	cut-clipboard
# 	-	changed

from gi.repository import Gtk, GLib, GdkPixbuf

class window(Gtk.Window):
	def __init__(self):
		super(window, self).__init__(title = "Entry Example")
		self.set_border_width(10)
		self.set_default_size(600, 400)

		vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
		self.add(vbox)

		entry = Gtk.Entry()
		entry.set_text("Default Entry with Max length")
		entry.connect("activate", self.on_activate)
		entry.set_max_length(255)
		vbox.pack_start(entry, True, True, 0)

		entry = Gtk.Entry()
		entry.set_text("Default Entry with visibility")
		entry.set_visibility(False)
		vbox.pack_start(entry, True, True, 0)

		entry = Gtk.Entry()
		entry.set_text("Default Entry without editable")
		entry.set_editable(False)
		vbox.pack_start(entry, True, True, 0)

		entry = Gtk.Entry()
		entry.set_text("Progress fraction Entry")
		entry.set_alignment(0.5)
		self.percent = 0
		timeout_id = GLib.timeout_add(500, self.progress, entry)
		vbox.pack_start(entry, True, True, 0)

		entry = Gtk.Entry()
		entry.set_text("Progress pulse Entry")
		entry.set_alignment(0.5)
		entry.set_progress_pulse_step(0.2)
		self.timeout_id = GLib.timeout_add(500, self.progress2, entry)
		vbox.pack_start(entry, True, True, 0)

		entry = Gtk.Entry()
		entry.set_text("Default Entry with Icon name")
		entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "package-supported")
		entry.set_icon_tooltip_text(Gtk.EntryIconPosition.PRIMARY, "I Love Ubuntu ^.^")
		vbox.pack_start(entry, True, True, 0)

		entry = Gtk.Entry()
		entry.set_text("Default Entry with Icon from file")
		icon = GdkPixbuf.Pixbuf.new_from_file("line.png")
		entry.set_icon_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, icon)
		vbox.pack_start(entry, True, True, 0)

	def on_activate(self, widget, data = None):
		print(widget.get_text())


	def progress(self, user_data):
		if self.percent <= 1:
			self.percent = self.percent + 0.1
		else:
			self.percent = 0
		user_data.set_progress_fraction(self.percent)
		return True

	def progress2(self, user_data):
		user_data.progress_pulse()
		return True

window = window()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
