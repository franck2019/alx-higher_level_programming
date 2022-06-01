#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into a
 * sorted singly linked list
 * @head: a pointer to the struct listint_t
 * @number: the number to insert
 *
 * Return:the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		tmp = *head;
		while (tmp->next != NULL && tmp->n < number)
			tmp = tmp->next;
		new->next = tmp->next;
		tmp->next = new;
	}
	
	return (new);
}
