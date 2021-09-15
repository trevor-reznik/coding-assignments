###
### Course: CSc 110
### Author: Christian Byrne
### Description: Accepts CPU GHz and numbers of cores.
###              Displays the CPU's performance status and indicates 
###              whether an upgrade is warranted. Uses scoring systems:
###              Core #: [2, 6, 8, 20]. GHz: [2.0, 2.5, 3.2]. Lower value is limiting.
###

inputs = [float(2)), float(2.7))]
responses = ["CPU could use an upgrade.", "is a low-performance CPU.", \
             "is a medium-performance CPU.", "is a high-performance CPU."]

scores = [3, 4]                 # 
for _ in [2, 6, 8, 20]:         # Put scores in list and 
    if int(inputs[1]) < _:      # iterate over score-thresholds.
        scores[1] -= 1          #
if scores[1] < 4:               # Only score GHz if cores < 20
    for _ in [2.0, 2.5, 3.2]:   #
        if inputs[0] < _:
            scores[0] -= 1

# Use lower score as index to call complementary responses-list element.
print("\nThat", responses[min(scores)])
