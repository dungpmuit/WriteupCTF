# Recipe Format

Sticker Booth reads commands from standard input, one command per line. Empty
lines and lines starting with `#` are ignored.

Item names are short labels used by later commands. Use simple names such as
`hero`, `top`, `badge`, or `sticker1`.

## Commands

### Photo

    photo NAME WIDTH HEIGHT RGBA_HEX

Adds a photo to the sheet. Pixels are row-major RGBA bytes written as hex.
The hex string must contain exactly `WIDTH * HEIGHT * 4` bytes.

Example:

    photo hero 2 1 336699ffcc8844ff

### Caption

    caption NAME TEXT

Adds a text caption. Everything after the name is used as the caption text.

Example:

    caption top best day ever

### Builtin

    builtin NAME heart|star|smile

Adds one of the built-in stickers.

Example:

    builtin badge heart

### Mono

    mono NAME

Applies the monochrome filter to a photo.

Example:

    mono hero

### Remove

    remove NAME

Removes an item from the current sheet.

Example:

    remove top

### Upload

    upload NAME HEX

Uploads a custom sticker payload as hex bytes.

Example:

    upload custom 41424344

### Print

    print

Prints the current sticker sheet.
