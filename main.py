d = int(input('Введите свое d: '))
A_volt = []
A_curr = []
phase_volt = []
phase_curr = []

with open('text.txt', 'r') as f:
    lines = f.readlines()
    for line in lines[3::]:
        text = line.strip().split(':')
        tmp = []
        for t in text:
            data = t.strip().split()
            tmp.extend(data)
        if tmp[0][0] == 'V':
            A_volt.append(float(tmp[2]))
            phase_volt.append(float(tmp[4][:-2]))
        else:
            A_curr.append(float(tmp[2]))
            phase_curr.append(float(tmp[4][:-2]))

with open('graphs.txt', 'w', encoding='utf-16') as f:
    f.write(f'd = linspace(0, {d}, 11);\n\n')
    f.write(f'A_volt = {A_volt};\n')
    f.write(f'phase_volt = {phase_volt};\n')
    f.write(f'A_curr = {list(reversed(A_curr))};\n')
    f.write(f'phase_curr = {list(reversed(phase_curr))};\n\n')
    f.write('fig = plot(d, A_volt);\nxlabel("d, мкм");\nylabel("U, V");\ngrid on;\nsaveas(fig, "A_volt", "png")\n')
    f.write('fig = plot(d, A_curr);\nxlabel("d, мкм");\nylabel("I, A");\ngrid on;\nsaveas(fig, "A_curr", "png")\n')
    f.write('fig = plot(d, phase_volt);\nxlabel("d, мкм");\nylabel("phase, degree");\ngrid on;\nsaveas(fig, "phase_volt", "png")\n')
    f.write('fig = plot(d, phase_curr);\nxlabel("d, мкм");\nylabel("phase, degree");\ngrid on;\nsaveas(fig, "phase_curr", "png")\n')
