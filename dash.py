#  ███╗    ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗    ███╗ #
#  ██╔╝    ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║    ╚██║ #
#  ██║     ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║     ██║ #
#  ██║     ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║     ██║ #
#  ███╗    ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║    ███║ #
#  ╚══╝    ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚══╝ #
#   Programmer Mmdrza.Com ~ Telegram Channel @mPython3 ~ ID Telegram @PyMmdrza ~ https://Mmdrza.Com      #
##########################################################################################################

import base64

e = b'aW1wb3J0IGNvZGVjcwppbXBvcnQgaGFzaGxpYgppbXBvcnQgdGhyZWFkaW5nCgppbXBvcnQgZWNkc2EKaW1wb3J0IHJlcXVlc3RzCmZyb20gaGR3YWxsZXQgaW1wb3J0IEhEV2FsbGV0CmZyb20gaGR3YWxsZXQuc3ltYm9scyBpbXBvcnQgREFTSCBhcyBTWU1CT0wKZnJvbSByZXF1ZXN0c19odG1sIGltcG9ydCBIVE1MU2Vzc2lvbgpmcm9tIHJpY2guY29uc29sZSBpbXBvcnQgQ29uc29sZQpmcm9tIHJpY2gucGFuZWwgaW1wb3J0IFBhbmVsCgpjb25zb2xlID0gQ29uc29sZSgpCmNvbnNvbGUuY2xlYXIoKQoKZmlsZXIgPSBpbnB1dCgnXG5bKl0gSnVzdCBFbnRlciB0aGUgRGVzaXJlZCBUZXh0IEZpbGUgTmFtZSBbSEVSRV0gOiAnKQoKbXlsaXN0ID0gW10KCmZpbGVuYW1lID0gc3RyKGZpbGVyICsgIi50eHQiKQp3aXRoIG9wZW4oZmlsZW5hbWUsIG5ld2xpbmU9JycsIGVuY29kaW5nPSd1dGYtOCcpIGFzIGY6CiAgICBmb3IgbGluZSBpbiBmOgogICAgICAgIG15bGlzdC5hcHBlbmQobGluZS5zdHJpcCgpKQoKCmNsYXNzIEJyYWluV2FsbGV0OgoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZW5lcmF0ZV9hZGRyZXNzX2Zyb21fcGFzc3BocmFzZShwYXNzcGhyYXNlKToKICAgICAgICBwcml2YXRlX2tleSA9IHN0cihoYXNobGliLnNoYTI1NigKICAgICAgICAgICAgcGFzc3BocmFzZS5lbmNvZGUoJ3V0Zi04JykpLmhleGRpZ2VzdCgpKQogICAgICAgIGFkZHJlc3MgPSBCcmFpbldhbGxldC5nZW5lcmF0ZV9hZGRyZXNzX2Zyb21fcHJpdmF0ZV9rZXkocHJpdmF0ZV9rZXkpCiAgICAgICAgcmV0dXJuIHByaXZhdGVfa2V5LCBhZGRyZXNzCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIGdlbmVyYXRlX2FkZHJlc3NfZnJvbV9wcml2YXRlX2tleShwcml2YXRlX2tleSk6CiAgICAgICAgcHVibGljX2tleSA9IEJyYWluV2FsbGV0Ll9fcHJpdmF0ZV90b19wdWJsaWMocHJpdmF0ZV9rZXkpCiAgICAgICAgYWRkcmVzcyA9IEJyYWluV2FsbGV0Ll9fcHVibGljX3RvX2FkZHJlc3MocHVibGljX2tleSkKICAgICAgICByZXR1cm4gYWRkcmVzcwoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBfX3ByaXZhdGVfdG9fcHVibGljKHByaXZhdGVfa2V5KToKICAgICAgICBwcml2YXRlX2tleV9ieXRlcyA9IGNvZGVjcy5kZWNvZGUocHJpdmF0ZV9rZXksICdoZXgnKQogICAgICAgIGtleSA9IGVjZHNhLlNpZ25pbmdLZXkuZnJvbV9zdHJpbmcoCiAgICAgICAgICAgIHByaXZhdGVfa2V5X2J5dGVzLCBjdXJ2ZT1lY2RzYS5TRUNQMjU2azEpLnZlcmlmeWluZ19rZXkKICAgICAgICBrZXlfYnl0ZXMgPSBrZXkudG9fc3RyaW5nKCkKICAgICAgICBrZXlfaGV4ID0gY29kZWNzLmVuY29kZShrZXlfYnl0ZXMsICdoZXgnKQogICAgICAgIGJpdGNvaW5fYnl0ZSA9IGInMDQnCiAgICAgICAgcHVibGljX2tleSA9IGJpdGNvaW5fYnl0ZSArIGtleV9oZXgKICAgICAgICByZXR1cm4gcHVibGljX2tleQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBfX3B1YmxpY190b19hZGRyZXNzKHB1YmxpY19rZXkpOgogICAgICAgIHB1YmxpY19rZXlfYnl0ZXMgPSBjb2RlY3MuZGVjb2RlKHB1YmxpY19rZXksICdoZXgnKQogICAgICAgICMgUnVuIFNIQTI1NiBmb3IgdGhlIHB1YmxpYyBrZXkKICAgICAgICBzaGEyNTZfYnBrID0gaGFzaGxpYi5zaGEyNTYocHVibGljX2tleV9ieXRlcykKICAgICAgICBzaGEyNTZfYnBrX2RpZ2VzdCA9IHNoYTI1Nl9icGsuZGlnZXN0KCkKICAgICAgICByaXBlbWQxNjBfYnBrID0gaGFzaGxpYi5uZXcoJ3JpcGVtZDE2MCcpCiAgICAgICAgcmlwZW1kMTYwX2Jway51cGRhdGUoc2hhMjU2X2Jwa19kaWdlc3QpCiAgICAgICAgcmlwZW1kMTYwX2Jwa19kaWdlc3QgPSByaXBlbWQxNjBfYnBrLmRpZ2VzdCgpCiAgICAgICAgcmlwZW1kMTYwX2Jwa19oZXggPSBjb2RlY3MuZW5jb2RlKHJpcGVtZDE2MF9icGtfZGlnZXN0LCAnaGV4JykKICAgICAgICBuZXR3b3JrX2J5dGUgPSBiJzAwJwogICAgICAgIG5ldHdvcmtfYml0Y29pbl9wdWJsaWNfa2V5ID0gbmV0d29ya19ieXRlICsgcmlwZW1kMTYwX2Jwa19oZXgKICAgICAgICBuZXR3b3JrX2JpdGNvaW5fcHVibGljX2tleV9ieXRlcyA9IGNvZGVjcy5kZWNvZGUoCiAgICAgICAgICAgIG5ldHdvcmtfYml0Y29pbl9wdWJsaWNfa2V5LCAnaGV4JykKICAgICAgICBzaGEyNTZfbmJwayA9IGhhc2hsaWIuc2hhMjU2KG5ldHdvcmtfYml0Y29pbl9wdWJsaWNfa2V5X2J5dGVzKQogICAgICAgIHNoYTI1Nl9uYnBrX2RpZ2VzdCA9IHNoYTI1Nl9uYnBrLmRpZ2VzdCgpCiAgICAgICAgc2hhMjU2XzJfbmJwayA9IGhhc2hsaWIuc2hhMjU2KHNoYTI1Nl9uYnBrX2RpZ2VzdCkKICAgICAgICBzaGEyNTZfMl9uYnBrX2RpZ2VzdCA9IHNoYTI1Nl8yX25icGsuZGlnZXN0KCkKICAgICAgICBzaGEyNTZfMl9oZXggPSBjb2RlY3MuZW5jb2RlKHNoYTI1Nl8yX25icGtfZGlnZXN0LCAnaGV4JykKICAgICAgICBjaGVja3N1bSA9IHNoYTI1Nl8yX2hleFs6OF0KICAgICAgICBhZGRyZXNzX2hleCA9IChuZXR3b3JrX2JpdGNvaW5fcHVibGljX2tleSArIGNoZWNrc3VtKS5kZWNvZGUoJ3V0Zi04JykKICAgICAgICB3YWxsZXQgPSBCcmFpbldhbGxldC5iYXNlNTgoYWRkcmVzc19oZXgpCiAgICAgICAgcmV0dXJuIHdhbGxldAoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBiYXNlNTgoYWRkcmVzc19oZXgpOgogICAgICAgIGFscGhhYmV0ID0gJzEyMzQ1Njc4OUFCQ0RFRkdISktMTU5QUVJTVFVWV1hZWmFiY2RlZmdoaWprbW5vcHFyc3R1dnd4eXonCiAgICAgICAgYjU4X3N0cmluZyA9ICcnCiAgICAgICAgbGVhZGluZ196ZXJvcyA9IGxlbihhZGRyZXNzX2hleCkgLSBsZW4oYWRkcmVzc19oZXgubHN0cmlwKCcwJykpCiAgICAgICAgYWRkcmVzc19pbnQgPSBpbnQoYWRkcmVzc19oZXgsIDE2KQogICAgICAgIHdoaWxlIGFkZHJlc3NfaW50ID4gMDoKICAgICAgICAgICAgZGlnaXQgPSBhZGRyZXNzX2ludCAlIDU4CiAgICAgICAgICAgIGRpZ2l0X2NoYXIgPSBhbHBoYWJldFtkaWdpdF0KICAgICAgICAgICAgYjU4X3N0cmluZyA9IGRpZ2l0X2NoYXIgKyBiNThfc3RyaW5nCiAgICAgICAgICAgIGFkZHJlc3NfaW50IC8vPSA1OAogICAgICAgIG9uZXMgPSBsZWFkaW5nX3plcm9zIC8vIDIKICAgICAgICBmb3Igb25lIGluIHJhbmdlKG9uZXMpOgogICAgICAgICAgICBiNThfc3RyaW5nID0gJzEnICsgYjU4X3N0cmluZwogICAgICAgIHJldHVybiBiNThfc3RyaW5nCgoKZGVmIE1tRHJ6YSgpOgogICAgdyA9IDAKICAgIGNvdW50ID0gMAoKICAgIGZvciBpIGluIHJhbmdlKGxlbihteWxpc3QpKToKICAgICAgICBjb3VudCArPSAxCiAgICAgICAgcGFzc3BocmFzZSA9IG15bGlzdFtpXQogICAgICAgIHdhbGxldCA9IEJyYWluV2FsbGV0KCkKICAgICAgICBwcml2YXRlX2tleSwgYWRkcmVzcyA9IHdhbGxldC5nZW5lcmF0ZV9hZGRyZXNzX2Zyb21fcGFzc3BocmFzZShwYXNzcGhyYXNlKQogICAgICAgIGhkd2FsbGV0OiBIRFdhbGxldCA9IEhEV2FsbGV0KHN5bWJvbD1TWU1CT0wpCiAgICAgICAgaGR3YWxsZXQuZnJvbV9wcml2YXRlX2tleShwcml2YXRlX2tleT1wcml2YXRlX2tleSkKICAgICAgICBhZGRyID0gaGR3YWxsZXQucDJzaF9hZGRyZXNzKCkKICAgICAgICB1cmxfbiA9IGYiaHR0cHM6Ly9kYXNoMi50cmV6b3IuaW8vYWRkcmVzcy97YWRkcn0iCiAgICAgICAgc2UgPSBIVE1MU2Vzc2lvbigpCiAgICAgICAgbm1wID0gc2UuZ2V0KHVybF9uKQogICAgICAgIE1hc3RlciA9IG5tcC5odG1sLnhwYXRoKCcvaHRtbC9ib2R5L21haW4vZGl2L2RpdlsyXS9kaXZbMV0vdGFibGUvdGJvZHkvdHJbM10vdGRbMl0nKQogICAgICAgIGJhbCA9IE1hc3RlclswXS50ZXh0CgogICAgICAgIGlmeGJ0YyA9ICcwIERBU0gnCiAgICAgICAgTW1kcnphUGFuZWwgPSBzdHIoJ1tnb2xkMSBvbiBncmV5MTVdVG90YWwgQ2hlY2tlZDogJyArICdbb3JhbmdlX3JlZDFdJyArIHN0cigKICAgICAgICAgICAgY291bnQpICsgJ1svXVtnb2xkMSBvbiBncmV5MTVdICcgKyAnIFdpbjonICsgJ1t3aGl0ZV0nICsgc3RyKHcpICsgJ1svXVtnb2xkMV0gIEJBTDpbYXF1YW1hcmluZTFdJyArIHN0cigKICAgICAgICAgICAgYmFsKSArICdcblsvXVtnb2xkMSBvbiBncmV5MTVdQWRkcjogJyArICdbd2hpdGVdICcgKyBzdHIoCiAgICAgICAgICAgIGFkZHJlc3MpICsgJ1tnb2xkMSBvbiBncmV5MTVdICAgICAgICAgICAgICAgICAgUGFzc3BocmFzZTogJyArICdbb3JhbmdlX3JlZDFdJyArIHN0cigKICAgICAgICAgICAgcGFzc3BocmFzZSkgKyAnWy9dXG5QUklWQVRFS0VZOiBbZ3JleTU0XScgKyBzdHIocHJpdmF0ZV9rZXkpICsgJ1svXScpCiAgICAgICAgc3R5bGUgPSAiZ29sZDEgb24gZ3JleTExIgogICAgICAgIGlmIGJhbCAhPSBpZnhidGM6CiAgICAgICAgICAgIGZ4ID0gb3Blbih1IkJpdGNvaW5XaW5uZXJfX19fX19fX18iICsgc3RyKGZpbGVyKSArICJfTU1EUlpBLnR4dCIsICJhIikKICAgICAgICAgICAgZngud3JpdGUoJ1xuQWRkcmVzcyBDb21wcmVzc2VkIDogJyArIGFkZHIgKyAnICBCYWwgPSAnICsgc3RyKGJhbCkpCiAgICAgICAgICAgIGZ4LndyaXRlKCdcblBhc3NwaHJhc2UgICAgICAgOiAnICsgcGFzc3BocmFzZSkKICAgICAgICAgICAgZngud3JpdGUoJ1xuUHJpdmF0ZSBLZXkgICAgICA6ICcgKyBwcml2YXRlX2tleSkKICAgICAgICAgICAgZngud3JpdGUoJ1xuQmFsYW5jZTogJyArIHN0cihiYWwpKQogICAgICAgICAgICBmeC53cml0ZSgnXG4tLS0tLS0tLS0tLS0tLS0tLS0gUHJvZ3JhbW1lciBNbWRyemEuQ29tIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbicpCiAgICAgICAgICAgIGZ4LmNsb3NlKCkKICAgICAgICAgICAgY29uc29sZS5wcmludCgKICAgICAgICAgICAgICAgIFBhbmVsKHN0cihNbWRyemFQYW5lbCksIHRpdGxlPSJbd2hpdGVdV2luIFdhbGxldCBbL10iLCBzdWJ0aXRsZT0iW2dyZWVuX3llbGxvdyBibGlua10gTW1kcnphLkNvbSBbL10iLAogICAgICAgICAgICAgICAgICAgICAgc3R5bGU9InJlZCIpLCBzdHlsZT1zdHlsZSwganVzdGlmeT0iZnVsbCIpCiAgICAgICAgICAgIHcgKz0gMQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGNvbnNvbGUucHJpbnQoZiJbcmVkMV1bU2NhbjpbY3lhbl17Y291bnR9Wy9jeWFuXSAtIFtncmVlbjFdRm91bmQ6Wy9ncmVlbjFdW2N5YW5de3d9Wy9jeWFuXV1bIERBU0ggQUREUjpbd2hpdGVdIHthZGRyfSBbL3doaXRlXV0gWyBWYWx1ZTpbY3lhbl17YmFsfVsvY3lhbl0gXSAjIFBhc3NwaHJhc2U6W3doaXRlXSB7cGFzc3BocmFzZX1bL3doaXRlXVsvcmVkMV0iKQogICAgICAgICAgICBjb250aW51ZQoKCk1tRHJ6YSgpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgTWFzdGVyID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9TW1EcnphKQogICAgTWFzdGVyLnN0YXJ0KCkKICAgIE1hc3Rlci5qb2luKCk='

exec(base64.b64decode(e).decode())






# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================
