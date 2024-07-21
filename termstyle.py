import sys

class TermStyle:
  # Note: to enable Coloring in command-powershell: 
  #   [REG ADD HKCU\CONSOLE /f /v VirtualTerminalLevel /t REG_DWORD /d 1]
  
  # =================== ANSI escape Codes
  reset   = u"\u001b[0m"
  bold    = u"\u001b[1m"
  italic  = '\33[3m'       # diff seq
  under   = u"\u001b[4m"
  select  = u"\u001b[7m"
  blink   = u"\033[5m"
  
  #cursor
  Up    =  u"\u001b[{n}A"
  down  = u"\u001b[{n}B"
  right = u"\u001b[{n}C"
  left  = u"\u001b[{n}D"
  back  = ""               # todo
  cret  = u"\r"
  # \u001b[ + n + E	Move cursor to beginning of line, n lines down
  # \u001b[ + n + F	Move cursor to beginning of line, n lines up
  # \u001b[ + n + G	Move cursor to column n
  # \u001b[ + n + ; + m + H	Move cursor to row n column m
  # \u001b[{s}	Save the current cursor position
  # \u001b[{u}	Restore the cursor to the last saved position
  
  #screen 
  #clr_upto_end = u"\u001b[0J"
  #clr_upto_begin= u"\u001b[1J"
  #clr_all= u"\u001b[2J"
  #clr_upto_line_end= u"\u001b[0K"
  #clr_upto_line_begin= u"\u001b[1K"
  #clr_line= u"\u001b[2K"


  # =================== color codes 0-255 (basic: see _generate for alls)
  black   = 0
  white   = 255
  gray    = 247
  red     = 1
  green   = 46
  blue    = 27
  orange  = 202
  yellow  = 226   #190
  # ...

  # =================== 256 color code 
  def fore(code:str) -> str:
    return u"\u001b[38;5;" + str(code) + "m"

  def back(code:str) -> str:
    return u"\u001b[48;5;" + str(code) + "m"
  
  def colors(fg:str, bk:str) -> str:
    return TermStyle.fore(fg)+TermStyle.back(bk)
  
  # =================== rgb encoding
  def fg_rgb(rgb:list) -> str:
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    
  def bk_rgb(rgb:list) -> str:
    return f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
  
  def print(style, value, wrap_italic=True):
    if (style):
      towrap = (wrap_italic and value and TermStyle.italic in style and
                 ("\u001b[48;5;" in style or TermStyle.select in style))
      if towrap:
        if value[0] != ' ':             
          value = ' '+value
        if value[len(value)-1] != ' ':
          value = value+' '
      value = style + value + TermStyle.style_end
    print(value)

  # =================== Color Picker Purpose Only
  def _generate_all():                  
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(TermStyle.fore(code) + code.ljust(4))
        print (TermStyle.reset)
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(TermStyle.back(code) + code.ljust(4))
        print (TermStyle.reset)
    
  # =================== Application Styles
  style_end = reset
  style_err = fore(yellow)+back(red)+bold+italic+blink
  style_wrn = fore(orange)+bold+italic
  style_ok  = fore(white)+back(green)+bold+italic
  style_tmr = fore(45)+back(17)+bold+italic