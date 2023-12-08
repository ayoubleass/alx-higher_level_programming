#include "lists.h"


/**
 * free_dlistint - Frees a dlistint_t list.
 * @head: Pointer to the head of the list.
 *
 * Description: Frees all nodes of a doubly linked list.
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;

	while (head != NULL)
	{
		tmp = head->next;
		free(head);
		head = tmp;
	}
}
