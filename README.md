# MBI Matplotlib styles

This is a Python module to provide an MBI-like `matplotlib` plotting style
inspired by the design of the MBI webpage: https://mbi-berlin.de

A minimal code example would look like this:

```python
import matplotlib.pyplot as plt
import mbistyles

with plt.style.context('mbistyles.base'):
    plt.figure()
    plt.plot(...)
    plt.show()
```

## Installation

You can use `pip` to directly install from the repository: 

    $ pip install git+https://github.com/dschick/mbistyles.git

## License

The project is licensed under the MIT license.
