import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "CMU Serif",
    "font.size": 12
})

def loss_plot(split):
    plt.figure(figsize=(4, 2.5))
    title_balanced = pd.read_csv(f'../data/logs/loss/{split}/title_balanced.csv')
    title_unbalanced = pd.read_csv(f'../data/logs/loss/{split}/title_unbalanced.csv')
    title_summary_balanced = pd.read_csv(f'../data/logs/loss/{split}/title_summary_balanced.csv')
    title_summary_unbalanced = pd.read_csv(f'../data/logs/loss/{split}/title_summary_unbalanced.csv')

    plt.plot(title_balanced['Step'][:-2], title_balanced['Value'][:-2], label='Title balanced')
    plt.plot(title_unbalanced['Step'][:-2], title_unbalanced['Value'][:-2], label='Title unbalanced')
    plt.plot(title_summary_balanced['Step'][:-2], title_summary_balanced['Value'][:-2], label='Title summary balanced')
    plt.plot(title_summary_unbalanced['Step'][:-2], title_summary_unbalanced['Value'][:-2],
             label='Title summary unbalanced')
    #plt.title(f'{split.capitalize()} loss evolution evolution')
    plt.legend(prop={'size': 9})
    plt.xlabel("Loss")
    plt.xlabel("Steps")
    #plt.show()
    plt.tight_layout(pad=0.2)
    plt.savefig(f'../output/loss_{split}_evolution.pdf')


def f1_plot():
    plt.figure(figsize=(4, 2.5))
    title_balanced = pd.read_csv('../data/logs/f1/title_balanced.csv')
    title_unbalanced = pd.read_csv('../data/logs/f1/title_unbalanced.csv')
    title_summary_balanced = pd.read_csv('../data/logs/f1/title_summary_balanced.csv')
    title_summary_unbalanced = pd.read_csv('../data/logs/f1/title_summary_unbalanced.csv')

    plt.plot(title_balanced['Step'][:-2], title_balanced['Value'][:-2], label='Title balanced')
    plt.plot(title_unbalanced['Step'][:-2], title_unbalanced['Value'][:-2], label='Title unbalanced')
    plt.plot(title_summary_balanced['Step'][:-2], title_summary_balanced['Value'][:-2], label='Title summary balanced')
    plt.plot(title_summary_unbalanced['Step'][:-2], title_summary_unbalanced['Value'][:-2],
             label='Title summary unbalanced')
    #plt.title("Valid micro-F1 evolution during training")
    plt.legend(prop={'size': 9})
    plt.xlabel("micro-F1 score")
    plt.xlabel("Steps")
    #plt.show()
    plt.tight_layout(pad=0.2)
    plt.savefig('../output/f1_evolution.pdf')


if __name__ == '__main__':
    f1_plot()
    loss_plot('train')
    loss_plot('valid')
