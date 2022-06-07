#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

//int size_listint(listint_t **head);
//int *extract_int(listint_t **head);
/**
 * is_palindrome - nction in C that checks
 * if a singly linked list is a palindrome.
 * @head: a pointer to pointer to a listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int *mylist = extract_int(head);
	int size = size_listint(head);
	int i, stop;

	stop = size / 2;
	for (i = 0; i <= stop; i++)
	{
		if (mylist[i] != mylist[size - 1 - i])
			return (0);
	}

	return (1);
}

/**
 * size_listint - gives the size of a listint_t list
 * @head: pointer to pointer of the first node of listint_t list      
 * Return: the size of the list or 0 if the list is NULL
 */
int size_listint(listint_t **head)
{
	listint_t *current;
	int size;

	size = 0;
	current = *head;
	while (current != NULL)
	{
		size++;
		current = current->next;
	}
	return (size);
}

/**
 * extract_int - retrieves every integer into a listsint_t list
 * @head: pointer to pointer of the first node of listint_t list
 * Return: a pointer to the adress of the list of int
 */
int *extract_int(listint_t **head)
{
	listint_t *current;
	int size = size_listint(head);
	int *mylist, i;

	mylist = malloc(sizeof(int) * size);

	if (mylist == NULL)
	{
		free(mylist);
		return (NULL);
	}

	current = *head;
	i = 0;
	while (current != NULL)
	{
		mylist[i] = current->n;
		i++;
		current = current->next;
	}

	return (mylist);
}
