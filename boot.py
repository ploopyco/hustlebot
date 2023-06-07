import supervisor
import storage
import usb_cdc

supervisor.set_usb_identification(
    manufacturer="Microsoft Corp.",
    product="Wired Keyboard 400",
    pid=0x0752,
    vid=0x045E
)

storage.disable_usb_drive()
usb_cdc.disable()
