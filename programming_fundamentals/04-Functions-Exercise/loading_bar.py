def loading_bar_status(percent):
    if percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{percent}% [{(percent//10) * '%'}{(100 - percent)// 10 * '.'}]\nStill loading..."


progress_percent = int(input()) # single integer number between 0 and 100 (inclusive)
# divisible by 10 without remainder (0, 10, 20, 30...)
loading_bar = loading_bar_status(progress_percent)
print(loading_bar)