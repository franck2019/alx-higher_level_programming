#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_dlistint - prints all elements of a dlistint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current;
	size_t n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

