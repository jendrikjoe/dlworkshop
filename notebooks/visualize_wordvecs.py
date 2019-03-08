import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

from typing import List


def make_word_vec_plot(words: List[str], word_vecs: List[np.ndarray]):
    grid = np.stack(word_vecs)

    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111)
    ax.imshow(grid, interpolation=None, cmap='bwr')
    ax.set_yticklabels([''] + words)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    fig.tight_layout()

    return fig


if __name__ == "__main__":
    words = ['king', 'queen', 'prince']
    # w_vecs = [np.ones(100) * -1, np.zeros(100), np.ones(100)]
    w_vecs = [np.random.randn(100) for _ in words]

    fig = make_word_vec_plot(words, w_vecs)

    fig.savefig('tmp.png')
