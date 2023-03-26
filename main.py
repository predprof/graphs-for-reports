import matplotlib.pyplot as plt
import numpy as np

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

fig, axes = plt.subplots(figsize=(15, 10), nrows=2, ncols=2)

axes[0, 0].set(title='Амплитуда напряжения', ylabel='U, V')
axes[0, 1].set(title='Фаза напряжения', ylabel='phase, degree')
axes[1, 0].set(title='Амплитуда тока', ylabel='I, A')
axes[1, 1].set(title='Фаза тока', ylabel='phase, degree')

x = np.linspace(0, d, 11)
graphs = [A_volt, phase_volt, list(reversed(A_curr)), list(reversed(phase_curr))]
for ax, gr in zip(axes.flat, graphs):
    ax.plot(x, gr)
    ax.set_xlabel("d, мкм")
plt.savefig('graphs.png')
plt.show()

# with open('graphs.txt', 'w', encoding='utf-16') as f:
#     f.write(f'd = linspace(0, {d}, 11);\n\n')
#     f.write(f'A_volt = {A_volt};\n')
#     f.write(f'phase_volt = {phase_volt};\n')
#     f.write(f'A_curr = {list(reversed(A_curr))};\n')
#     f.write(f'phase_curr = {list(reversed(phase_curr))};\n\n')
#     f.write('fig = plot(d, A_volt);\nxlabel("d, мкм");\nylabel("U, V");\ngrid on;\nsaveas(fig, "A_volt", "png")\n')
#     f.write('fig = plot(d, A_curr);\nxlabel("d, мкм");\nylabel("I, A");\ngrid on;\nsaveas(fig, "A_curr", "png")\n')
#     f.write('fig = plot(d, phase_volt);\nxlabel("d, мкм");\nylabel("phase, degree");\ngrid on;\nsaveas(fig, "phase_volt", "png")\n')
#     f.write('fig = plot(d, phase_curr);\nxlabel("d, мкм");\nylabel("phase, degree");\ngrid on;\nsaveas(fig, "phase_curr", "png")\n')
