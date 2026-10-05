import matplotlib.pyplot as plt
import seaborn as sns


def barplot(data, x, y, estimator='sum', hue=None, figsize=(12, 6), order_by_y=True):
    plt.figure(figsize=figsize)
    order = None

    if order_by_y:
        order = (data.groupby(x)[y].sum().sort_values(ascending=False).index)

    sns.barplot(data=data, x=x, y=y, hue=hue,
                estimator=estimator, errorbar=None, order=order)
    plt.xticks(rotation=60, ha='right')
    plt.show()


def lineplot(df, x, y, estimator='sum', figsize=(12, 6), hue=None, title=None):
    plt.figure(figsize=figsize)
    ax = sns.lineplot(data=df, x=x, y=y, hue=hue,
                      estimator=estimator, errorbar=None)
    ax.set_xticks(sorted(df[x].unique()))
    if title:
        ax.set_title(title)
    plt.show()


def heatmap(data, figsize=(8, 6)):
    plt.figure(figsize=figsize)
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', center=0)
    plt.tight_layout()
    plt.show()
