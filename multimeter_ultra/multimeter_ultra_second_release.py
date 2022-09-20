import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk

ws = Tk()
import pandas as pd


class rekenwerk:
    def Replace(str1):
        maketrans = str1.maketrans
        final = str1.translate(maketrans(",.", ".,", " "))
        return final.replace(",", ", ")

    def makeform(root, fields):
        entries = {}
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=22, text=field + ": ", anchor="w")
            ent = tk.Entry(row)
            ent.insert(0, "0")
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries[field] = ent
        return entries

    def pw_µA_DC():
        fields = ("micro Ampere", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace((entries["micro Ampere"].get())))
            if C > 0 and C <= 4000:
                D = 0.001 * C + 4 * 0.1
            elif C > 4000 and C <= 400000:
                D = 0.001 * C + 4 * 10
            elif C > 400000 and C <= 1000000:
                D = 0.003 * C + 4 * 1000
            elif C > 1000000 and C <= 5000000:
                D = 0.01 * C + 4 * 1000
            elif C > 5000000 and C <= 10000000:
                D = 0.03 * C + 10 * 1000
            F = ":  ({}".format(C) + " ± {}".format(D) + ") µA"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_mA_DC():
        fields = ("mili Ampere", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["mili Ampere"].get()))
            if C > 0 and C <= 4:
                D = 0.001 * C + 4 * 0.0001
            elif C > 4 and C <= 400:
                D = 0.001 * C + 4 * 0.01
            elif C > 400 and C <= 1000:
                D = 0.003 * C + 4 * 1
            elif C > 1000 and C <= 5000:
                D = 0.01 * C + 4 * 1
            elif C > 5000 and C <= 10000:
                D = 0.03 * C + 10 * 1
            F = ":  ({}".format(C) + " ± {}".format(D) + ") mA"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_Am_DC():
        fields = ("Ampere", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["Ampere"].get()))
            if C > 0 and C <= 0.004:
                D = 0.001 * C + 4 * 0.0000001
            elif C > 0.004 and C <= 0.4:
                D = 0.001 * C + 4 * 0.00001
            elif C > 0.4 and C <= 1:
                D = 0.003 * C + 4 * 0.001
            elif C > 1 and C <= 5:
                D = 0.01 * C + 4 * 0.001
            elif C > 5 and C <= 10:
                D = 0.03 * C + 10 * 0.001
            F = ":  ({}".format(C) + " ± {}".format(D) + ") A"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_µA_AC():
        fields = ("micro Ampere", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["micro Ampere"].get()))
            if C > 0 and C <= 1000:
                D = 0.005 * C + 4 * 1
            elif C > 1000 and C <= 100000:
                D = 0.005 * C + 4 * 100
            elif C > 100000 and C <= 1000000:
                D = 0.008 * C + 4 * 10000
            elif C > 1000000 and C <= 5000000:
                D = 0.015 * C + 4 * 10000
            elif C > 5000000 and C <= 10000000:
                D = 0.03 * C + 4 * 10000
            F = ":  ({}".format(C) + " ± {}".format(D) + ") µA"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_mA_AC():
        fields = ("mili Ampere", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["mili Ampere"].get()))
            if C > 0 and C <= 1:
                D = 0.005 * C + 4 * 0.001
            elif C > 1 and C <= 100:
                D = 0.005 * C + 4 * 0.1
            elif C > 100 and C <= 1000:
                D = 0.008 * C + 4 * 10
            elif C > 1000 and C <= 5000:
                D = 0.015 * C + 4 * 10
            elif C > 5000 and C <= 10000:
                D = 0.03 * C + 4 * 10
            F = ":  ({}".format(C) + " ± {}".format(D) + ") mA"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_Am_AC():
        fields = ("Ampere", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["Ampere"].get()))
            if C > 0 and C <= 0.001:
                D = 0.005 * C + 4 * 0.000001
            elif C > 0.001 and C <= 0.1:
                D = 0.005 * C + 4 * 0.0001
            elif C > 0.1 and C <= 1:
                D = 0.008 * C + 4 * 0.01
            elif C > 1 and C <= 5:
                D = 0.015 * C + 4 * 0.01
            elif C > 5 and C <= 10:
                D = 0.03 * C + 4 * 0.01
            F = ":  ({}".format(C) + " ± {}".format(D) + ") A"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_µV_DC():
        fields = ("micro Volt", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["micro Volt"].get()))
            if C > 0 and C <= 400000:
                D = 0.0008 * C + 4 * 10
            elif C > 400000 and C <= 4000000:
                D = 0.0008 * C + 4 * 100
            elif C > 4000000 and C <= 40000000:
                D = 0.0008 * C + 4 * 1000
            elif C > 40000000 and C <= 400000000:
                D = 0.0008 * C + 4 * 10000
            elif C > 400000000 and C <= 1000000000:
                D = 0.0009 * C + 4 * 100000
            F = ":  ({}".format(C) + " ± {}".format(D) + ") µV"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_mV_DC():
        fields = ("mili Volt", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["mili Volt"].get()))
            if C > 0 and C <= 400:
                D = 0.0008 * C + 4 * 0.01
            elif C > 400 and C <= 4000:
                D = 0.0008 * C + 4 * 0.1
            elif C > 4000 and C <= 40000:
                D = 0.0008 * C + 4 * 1
            elif C > 40000 and C <= 400000:
                D = 0.0008 * C + 4 * 10
            elif C > 400000 and C <= 1000000:
                D = 0.0009 * C + 4 * 100
            F = ":  ({}".format(C) + " ± {}".format(D) + ") mV"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_Vm_DC():
        fields = ("Volt", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["Volt"].get()))
            if C > 0 and C <= 0.4:
                D = 0.0008 * C + 4 * 0.00001
            elif C > 0.4 and C <= 4:
                D = 0.0008 * C + 4 * 0.0001
            elif C > 4 and C <= 40:
                D = 0.0008 * C + 4 * 0.001
            elif C > 40 and C <= 400:
                D = 0.0008 * C + 4 * 0.01
            elif C > 400 and C <= 1000:
                D = 0.0009 * C + 4 * 0.1
            F = ":  ({}".format(C) + " ± {}".format(D) + ") V"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_µV_AC():
        fields = ("Hertz", "micro Volt", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["Hertz"].get()))
            D = float(rekenwerk.Replace(entries["micro Volt"].get()))
            if C > 45 and C <= 400:
                if D > 0 and D <= 400000:
                    E = 0.005 * D + 4 * 100
                elif D > 400000 and D <= 4000000:
                    E = 0.005 * D + 4 * 1000
                elif D > 4000000 and D <= 40000000:
                    E = 0.005 * D + 4 * 10000
                elif D > 40000000 and D <= 400000000:
                    E = 0.005 * D + 4 * 100000
                elif D > 400000000 and D <= 750000000:
                    D = 0.01 * D + 4 * 1000000

            elif C > 400 and C <= 5000:
                if D > 0 and D <= 400000:
                    E = 0.01 * D + 4 * 100
                elif D > 400000 and D <= 4000000:
                    E = 0.02 * D + 4 * 1000
                elif D > 4000000 and D <= 40000000:
                    E = 0.02 * D + 4 * 10000
                elif D > 40000000 and D <= 400000000:
                    E = 0.03 * D + 4 * 100000

            elif C > 5000 and C <= 20000:
                if D > 0 and D <= 400000:
                    E = 0.03 * D + 4 * 100
                elif D > 400000 and D <= 4000000:
                    E = 0.05 * D + 4 * 1000
                elif D > 4000000 and D <= 40000000:
                    E = 0.05 * D + 4 * 10000
                elif D > 40000000 and D <= 400000000:
                    E = 0.05 * D + 4 * 100000

            F = ":  ({}".format(D) + " ± {}".format(E) + ") µV"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_mV_AC():
        fields = ("Hertz", "mili Volt", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["Hertz"].get()))
            D = float(rekenwerk.Replace(entries["mili Volt"].get()))
            if C > 45 and C <= 400:
                if D > 0 and D <= 400:
                    E = 0.005 * D + 4 * 0.1
                elif D > 400 and D <= 4000:
                    E = 0.005 * D + 4 * 1
                elif C > 4000 and D <= 40000:
                    E = 0.005 * D + 4 * 10
                elif D > 40000 and D <= 400000:
                    E = 0.005 * D + 4 * 100
                elif D > 400000 and D <= 750000:
                    E = 0.01 * D + 4 * 1000

            elif C > 400 and C <= 5000:
                if D > 0 and D <= 400:
                    E = 0.01 * D + 4 * 0.1
                elif D > 400 and D <= 4000:
                    E = 0.02 * D + 4 * 1
                elif D > 4000 and D <= 40000:
                    E = 0.02 * D + 4 * 10
                elif D > 40000 and D <= 400000:
                    E = 0.03 * D + 4 * 100

            elif C > 5000 and C <= 20000:
                if D > 0 and D <= 400:
                    E = 0.03 * D + 4 * 0.1
                elif D > 400 and D <= 4000:
                    E = 0.05 * D + 4 * 1
                elif D > 4000 and D <= 40000:
                    E = 0.05 * D + 4 * 10
                elif D > 40000 and D <= 400000:
                    E = 0.05 * D + 4 * 100

            F = ":  ({}".format(D) + " ± {}".format(E) + ") mV"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def pw_Vm_AC():
        fields = ("Hertz", "Volt", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["Hertz"].get()))
            D = float(rekenwerk.Replace(entries["Volt"].get()))
            if C > 45 and C <= 400:
                if D > 0 and D <= 0.4:
                    E = 0.005 * D + 4 * 0.0001
                elif D > 0.4 and D <= 4:
                    E = 0.005 * D + 4 * 0.001
                elif D > 4 and D <= 40:
                    E = 0.005 * D + 4 * 0.01
                elif D > 40 and D <= 400:
                    E = 0.005 * D + 4 * 0.1
                elif D > 400 and D <= 750:
                    E = 0.01 * D + 4 * 1

            elif C > 400 and C <= 5000:
                if D > 0 and D <= 0.4:
                    E = 0.01 * D + 4 * 0.0001
                elif D > 0.4 and D <= 4:
                    E = 0.02 * D + 4 * 0.001
                elif D > 4 and D <= 40:
                    E = 0.02 * D + 4 * 0.01
                elif D > 40 and D <= 400:
                    E = 0.03 * D + 4 * 0.1

            elif C > 5000 and C <= 20000:
                if D > 0 and D <= 0.4:
                    E = 0.03 * D + 4 * 0.0001
                elif D > 0.4 and D <= 4:
                    E = 0.05 * D + 4 * 0.001
                elif D > 4 and D <= 40:
                    E = 0.05 * D + 4 * 0.01
                elif D > 40 and D <= 400:
                    E = 0.05 * D + 4 * 0.1

            F = ":  ({}".format(D) + " ± {}".format(E) + ") V"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def popup_win_mR():
        fields = ("mili Ohm", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["mili Ohm"].get()))
            if C > 0 and C <= 400000:
                D = 0.0015 * C + 6 * 10
            elif C > 400000 and C <= 4000000:
                D = 0.001 * C + 4 * 100
            elif C > 4000000 and C <= 40000000:
                D = 0.001 * C + 4 * 1000
            elif C > 40000000 and C <= 400000000:
                D = 0.0015 * C + 4 * 10000
            elif C > 400000000 and C <= 4000000000:
                D = 0.003 * C + 6 * 100000
            elif C > 4000000000 and C <= 40000000000:
                D = 0.01 * C + 10 * 1000000
            F = ":  ({}".format(C) + " ± {}".format(D) + ") mΩ"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def popup_win_Rm():
        fields = ("Ohm", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["Ohm"].get()))
            if C > 0 and C <= 400:
                D = 0.0015 * C + 6 * 0.01
            elif C > 400 and C <= 4000:
                D = 0.001 * C + 4 * 0.1
            elif C > 4000 and C <= 40000:
                D = 0.001 * C + 4 * 1
            elif C > 40000 and C <= 400000:
                D = 0.0015 * C + 4 * 10
            elif C > 400000 and C <= 4000000:
                D = 0.003 * C + 6 * 100
            elif C > 4000000 and C <= 40000000:
                D = 0.01 * C + 10 * 1000
            F = ":  ({}".format(C) + " ± {}".format(D) + ") Ω"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def popup_win_kR():
        fields = ("kilo Ohm", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["kilo Ohm"].get()))
            if C > 0 and C <= 0.4:
                D = 0.0015 * C + 6 * 0.00001
            elif C > 0.4 and C <= 4:
                D = 0.001 * C + 4 * 0.0001
            elif C > 4 and C <= 40:
                D = 0.001 * C + 4 * 0.001
            elif C > 40 and C <= 400:
                D = 0.0015 * C + 4 * 0.01
            elif C > 400 and C <= 4000:
                D = 0.003 * C + 6 * 0.1
            elif C > 4000 and C <= 40000:
                D = 0.01 * C + 10 * 1
            F = ":  ({}".format(C) + " ± {}".format(D) + ") kΩ"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()

    def popup_win_MR():
        fields = ("Mega Ohm", "onnauwkeurigheid")

        def v1(entries):
            C = float(rekenwerk.Replace(entries["Mega Ohm"].get()))
            if C > 0 and C <= 0.0004:
                D = 0.0015 * C + 6 * 0.00000001
            elif C > 0.0004 and C <= 0.004:
                D = 0.001 * C + 4 * 0.0000001
            elif C > 0.004 and C <= 0.04:
                D = 0.001 * C + 4 * 0.000001
            elif C > 0.04 and C <= 0.4:
                D = 0.0015 * C + 4 * 0.00001
            elif C > 0.4 and C <= 4:
                D = 0.003 * C + 6 * 0.0001
            elif C > 4 and C <= 40:
                D = 0.01 * C + 10 * 0.001
            F = ":  ({}".format(C) + " ± {}".format(D) + ") MΩ"
            entries["onnauwkeurigheid"].delete(0, tk.END)
            entries["onnauwkeurigheid"].insert(0, F)

        rekenwerk.makeform

        root = tk.Tk()
        root.title("de onnauwkeurigheid")
        ents = rekenwerk.makeform(root, fields)
        b1 = tk.Button(
            root, text="bereken", bg="#CD853F", command=(lambda e=ents: v1(e))
        )
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()


class DMM1:
    ws.title(
        "DMM onzekerheid berekenen, door Jort Joris Leroij   Technische Natuurkunde - Delft"
    )
    ws.geometry("2400x1200")
    ws.config(bg="#5FB691")
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="black", background="#CD853F")
    style.configure(
        "W.TButton",
        width=20,
        foreground="black",
        background="#CD853F",
        font=("Helvetica 16 bold"),
    )
    l = tk.Label(
        text="de onnauwkeurigheid berekenen van de digitale multimeter",
        borderwidth=3,
        relief="ridge",
        font=("Helvetica 20 bold"),
        bg="#DAA520",
    ).pack(padx=5, pady=20)

    label2 = Label()
    button_µA = Button()
    button_mA = Button()
    button_A = Button()
    button_µU = Button()
    button_mU = Button()
    button_U = Button()
    button_mΩ = Button()
    button_Ω = Button()
    button_kΩ = Button()
    button_MΩ = Button()

    def HOME():
        DMM1.button_µA.pack_forget()
        DMM1.button_mA.pack_forget()
        DMM1.button_A.pack_forget()
        DMM1.button_µU.pack_forget()
        DMM1.button_mU.pack_forget()
        DMM1.button_U.pack_forget()
        DMM1.button_mΩ.pack_forget()
        DMM1.button_Ω.pack_forget()
        DMM1.button_kΩ.pack_forget()
        DMM1.button_MΩ.pack_forget()
        DMM1.label2.pack_forget()

    def pw_A_DC():
        DMM1.HOME()
        DMM1.label2 = Label(
            text="selecteer een grootheid voor het direct current amperage",
            relief="ridge",
            font=("Helvetica 15 bold"),
            style="BW.TLabel",
        )
        DMM1.label2.pack(pady=20)

        DMM1.button_µA = Button(
            text="µA", style="W.TButton", cursor="pirate", command=rekenwerk.pw_µA_DC
        )
        DMM1.button_mA = Button(
            text="mA", style="W.TButton", cursor="pirate", command=rekenwerk.pw_mA_DC
        )
        DMM1.button_A = Button(
            text="A", style="W.TButton", cursor="pirate", command=rekenwerk.pw_Am_DC
        )

        DMM1.button_µA.pack(pady=10)
        DMM1.button_mA.pack(pady=10)
        DMM1.button_A.pack(pady=10)

    def pw_A_AC():
        DMM1.HOME()
        DMM1.label2 = Label(
            text="selecteer een grootheid voor het alternating current amperage",
            style="BW.TLabel",
            borderwidth=4,
            relief="ridge",
            font=("Helvetica 15 bold"),
        )
        DMM1.label2.pack(pady=20)

        DMM1.button_µA = Button(
            text="µA", style="W.TButton", cursor="pirate", command=rekenwerk.pw_µA_AC
        )
        DMM1.button_mA = Button(
            text="mA", style="W.TButton", cursor="pirate", command=rekenwerk.pw_mA_AC
        )
        DMM1.button_A = Button(
            text="A", style="W.TButton", cursor="pirate", command=rekenwerk.pw_Am_AC
        )

        DMM1.button_µA.pack(pady=10)
        DMM1.button_mA.pack(pady=10)
        DMM1.button_A.pack(pady=10)

    def pw_V_DC():
        DMM1.HOME()
        DMM1.label2 = Label(
            text="selecteer een grootheid voor het direct current voltage",
            style="BW.TLabel",
            borderwidth=4,
            relief="ridge",
            font=("Helvetica 15 bold"),
        )
        DMM1.label2.pack(pady=20)

        DMM1.button_µU = Button(
            text="µV", style="W.TButton", cursor="pirate", command=rekenwerk.pw_µV_DC
        )
        DMM1.button_mU = Button(
            text="mV", style="W.TButton", cursor="pirate", command=rekenwerk.pw_mV_DC
        )
        DMM1.button_U = Button(
            text="V", style="W.TButton", cursor="pirate", command=rekenwerk.pw_Vm_DC
        )

        DMM1.button_µU.pack(pady=10)
        DMM1.button_mU.pack(pady=10)
        DMM1.button_U.pack(pady=10)

    def pw_V_AC():
        DMM1.HOME()
        DMM1.label2 = Label(
            text="selecteer een grootheid voor het alternating current voltage",
            style="BW.TLabel",
            borderwidth=4,
            relief="ridge",
            font=("Helvetica 15 bold"),
        )
        DMM1.label2.pack(pady=20)

        DMM1.button_µU = Button(
            text="µV", style="W.TButton", cursor="pirate", command=rekenwerk.pw_µV_AC
        )
        DMM1.button_mU = Button(
            text="mV", style="W.TButton", cursor="pirate", command=rekenwerk.pw_mV_AC
        )
        DMM1.button_U = Button(
            text="V", style="W.TButton", cursor="pirate", command=rekenwerk.pw_Vm_AC
        )

        DMM1.button_µU.pack(pady=10)
        DMM1.button_mU.pack(pady=10)
        DMM1.button_U.pack(pady=10)

    def pw_R():
        DMM1.HOME()
        DMM1.label2 = Label(
            text="selecteer een grootheid voor de weerstand",
            style="BW.TLabel",
            borderwidth=4,
            relief="ridge",
            font=("Helvetica 15 bold"),
        )
        DMM1.label2.pack(pady=20)

        DMM1.button_mΩ = Button(
            text="mΩ",
            style="W.TButton",
            cursor="pirate",
            command=rekenwerk.popup_win_mR,
        )
        DMM1.button_Ω = Button(
            text="Ω", style="W.TButton", cursor="pirate", command=rekenwerk.popup_win_Rm
        )
        DMM1.button_kΩ = Button(
            text="kΩ",
            style="W.TButton",
            cursor="pirate",
            command=rekenwerk.popup_win_kR,
        )
        DMM1.button_MΩ = Button(
            text="MΩ",
            style="W.TButton",
            cursor="pirate",
            command=rekenwerk.popup_win_MR,
        )

        DMM1.button_mΩ.pack(pady=10)
        DMM1.button_Ω.pack(pady=10)
        DMM1.button_kΩ.pack(pady=10)
        DMM1.button_MΩ.pack(pady=10)

    def startknoppen():
        Button(
            ws,
            text="Amperage (DC)",
            style="W.TButton",
            cursor="circle",
            command=DMM1.pw_A_DC,
        ).pack(pady=10)
        Button(
            ws,
            text="Amperage (AC)",
            style="W.TButton",
            cursor="circle",
            command=DMM1.pw_A_AC,
        ).pack(pady=10)
        Button(
            ws,
            text="voltage      (DC)",
            style="W.TButton",
            cursor="circle",
            command=DMM1.pw_V_DC,
        ).pack(pady=10)
        Button(
            ws,
            text="voltage      (AC)",
            style="W.TButton",
            cursor="circle",
            command=DMM1.pw_V_AC,
        ).pack(pady=10)
        Button(
            ws,
            text="weerstand        ",
            style="W.TButton",
            cursor="circle",
            command=DMM1.pw_R,
        ).pack(pady=10)


DMM1.startknoppen()
ws.mainloop()
