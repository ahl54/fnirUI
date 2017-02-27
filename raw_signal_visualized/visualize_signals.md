

```python
import os
import ast
import matplotlib.pyplot as plt

raw_signal_path = """raw_signal/"""

for filename in os.listdir(raw_signal_path):
        data = []
        if (not filename.endswith('.ipynb_checkpoints')):
            
            # fetch signal from file
            with open(raw_signal_path + filename) as fin:
                data = ast.literal_eval(fin.read())
               
            # plot signal
            plt.plot(*zip(*data))
            plt.title('Signal ' + filename)
            plt.ylabel('Amplitude (mV)')
            plt.xlabel('Time (seconds)')
            plt.grid()
            plt.show()
```


![png](output_0_0.png)



![png](output_0_1.png)



![png](output_0_2.png)



![png](output_0_3.png)



![png](output_0_4.png)



![png](output_0_5.png)



![png](output_0_6.png)



![png](output_0_7.png)



![png](output_0_8.png)



![png](output_0_9.png)



![png](output_0_10.png)



![png](output_0_11.png)



```python

```
