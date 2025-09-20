#include <stdio.h>

int main() {
    int N;
    int first = 1; // to avoid printing extra blank line at the very end
    
    while (scanf("%d", &N) != EOF) {
        if (!first) {
            printf("\n"); // blank line between trees
        }
        first = 0;

        // Print tree leaves
        for (int i = 1; i <= N; i += 2) {
            int spaces = (N - i) / 2;
            for (int j = 0; j < spaces; j++) printf(" ");
            for (int j = 0; j < i; j++) printf("*");
            printf("\n");
        }

        // Print trunk: one "*" centered
        int spaces = (N - 1) / 2;
        for (int j = 0; j < spaces; j++) printf(" ");
        printf("*\n");

        // Print trunk: three "*" centered
        spaces = (N - 3) / 2;
        for (int j = 0; j < spaces; j++) printf(" ");
        printf("***\n");
    }
    return 0;
}


