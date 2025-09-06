import matplotlib.pyplot as plt

class Dashboard:
    def grafico_pizza(self, despesas):
        labels = [d[0] for d in despesas]
        valores = [d[1] for d in despesas]

        plt.pie(valores, labels=labels, autopct='%1.1f%%')
        plt.title("Distribuição de Despesas")
        plt.show()

    def grafico_histograma(self, despesas):
        valores = [d[1] for d in despesas]

        plt.hist(valores, bins=5, edgecolor='black')
        plt.title("Histograma de Despesas")
        plt.xlabel("Valor")
        plt.ylabel("Frequência")
        plt.show()
