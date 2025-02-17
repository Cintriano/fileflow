# Gerenciador de Fotos 📸

Este projeto foi criado para facilitar meu workflow de edição e gerenciamento de fotos, permitindo lidar com grandes volumes de arquivos em poucos segundos.

## ✨ Funcionalidades

-   **Renomear arquivos** automaticamente com base em metadados.
-   **Conversão de arquivos** para diferentes formatos.
-   **Registro das execuções** para rastreamento.
-   **Busca nos registros** para fácil recuperação de informações.

## 📂 Renomeação de Arquivos

O programa renomeia os arquivos seguindo um padrão predefinido (**dd.mm.aaaa_XXXXX**), onde a data é extraída automaticamente dos metadados sempre que possível. Caso os metadados não estejam disponíveis, outras fontes de informação podem ser utilizadas. Se nenhuma informação de data for encontrada e eu também não souber essa informação, o arquivo será renomeado sem a data.

Para lidar com diferentes situações, o sistema considera três cenários possíveis:

### ✅ Melhor Caso (Metadados Preservados)

Esse caso se refere a arquivos que vem direetamente do dispositivo de origem, isso significa que todos os metadados estão preservados (como data, hora e dispositivo), permitindo uma renomeação precisa. Portanto o programa extrai os dados necessarios diretamente dos metadados e realiza a renomeação.

### 📑 Caso Médio (Nome do Arquivo)
Quando o arquivo não contém metadados suficientes para a renomeação ideal, o programa utiliza as informações presentes no próprio nome do arquivo (**20250217_82713**, por exemplo).

Nesse caso, ele extrai e limpa os dados relevantes do nome original e os utiliza para realizar a renomeação seguindo o padrão estabelecido.

### ❓ Pior Caso (Sem Informações Disponíveis)
Esse caso se aplica a arquivos que não possuem nenhuma informação de data disponível, seja nos metadados ou no nome do arquivo.

Como o programa não tem dados suficientes para determinar uma data, ele segue um padrão específico para esses casos, utilizando um formato genérico, definido **IMG_94264**.
