import qrcode as qr

img  = qr.make("https://www.youtube.com/watch?v=hxHhcHmxPFY")
# img  = qr.make("You are Strong Men")
img.save("leetcode_problem.png")
print("done")