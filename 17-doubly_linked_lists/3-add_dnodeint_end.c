#include "lists.h"


/**
 * add_dnodeint_end - Adds a new node at the end of a dlistint_t list.
 * @head: Pointer to the address of the head of the list.
 * @n: Value to be assigned to the new node.
 *
 * Return: Address of the new element, or NULL if it fails.
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_list = NULL, *cpy = *head;

	new_list = malloc(sizeof(dlistint_t));
	if (new_list == NULL)
		return (NULL);
	new_list->n = n;
	new_list->next = NULL;

	if (*head == NULL)
		*head = new_list;
	else
	{
		while (cpy->next != NULL)
		{
			cpy = cpy->next;
		}
		new_list->prev = cpy;
		cpy->next = new_list;
	}
	return (new_list);
}
