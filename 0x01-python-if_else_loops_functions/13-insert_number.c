#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - Inserts a new node with the given number
 * into a sorted linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The value to be inserted into the linked list.
 *
 * Return: Pointer to the newly inserted node or NULL on failure.
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newList = malloc(sizeof(listint_t));
	listint_t *copy = *head;
	listint_t *prev = NULL;

	if (newList == NULL)
		return (NULL);

	while (copy != NULL && copy->n < number)
	{
		prev = copy;
		newList->n = number;
		newList->next = NULL;
		copy = copy->next;
	}

	if (prev  == NULL)
	{
		newList->next = *head;
		*head = newList;

	}
	else
	{
		prev->next = newList;
		newList->next = copy;
	}
	return (newList);
}
