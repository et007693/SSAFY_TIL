class StringRepeater:
    def repeat_string(self, cnt, string):
        for _ in range(cnt):
            print(string)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
