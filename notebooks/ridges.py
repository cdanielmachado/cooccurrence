import seaborn as sns
import matplotlib.pyplot as plt

sizes = [2,4,6,8,10,15,20,25,30,40]
types = ["random", "bin_rnd_01", "bin_rnd_001"]
palette = {"random": '#cccccc', "bin_rnd_01": '#ed7e17', "bin_rnd_001": '#1ba055'}


def ridges(df, var, xlim, xlabel):
    sns.set(rc={"axes.facecolor": (0, 0, 0, 0)})

    f, axs = plt.subplots(len(sizes), 1, figsize=(3, 6))
    for i, size in enumerate(sizes):
        for commtype in types:
            res = df.query("size == @size and type == @commtype")
            sns.kdeplot(res[var], shade=True, ax=axs[i], alpha=0.5, legend=False, clip_on=True, color=palette[commtype])
        axs[i].set_yticks([])
        if i < len(sizes) -1:
            axs[i].set_xticks([])
        axs[i].set_xlim(xlim)
        axs[i].axhline()
        axs[i].text(-0.08, 0.2, str(size), ha="right", va="center", transform=axs[i].transAxes)

        if i == len(sizes) -1:
            axs[i].set_xlabel(xlabel)

    f.subplots_adjust(hspace=-0.5)
    sns.despine(fig=f, bottom=True, left=True)
    return axs