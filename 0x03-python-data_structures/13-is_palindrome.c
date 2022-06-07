#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

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
