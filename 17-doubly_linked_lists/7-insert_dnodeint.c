#include "lists.h"


/**
 * insert_dnodeint_at_index - Inserts a new node at a given
 * position in a dlistint_t list.
 * @h: Pointer to the address of the head of the list.
 * @idx: Index at which the new node should be inserted.
 * @n: Value to be assigned to the new node.
 *
 * Return: Address of the new element, or NULL if it fails.
 */

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new_list = NULL, *prev, *next, *cpy;
	unsigned int position  = 0;

	cpy = *h;
	while (cpy != NULL)
	{
		if (position == idx - 1)
		{
			prev = cpy;
			next = cpy->next;
			new_list = malloc(sizeof(dlistint_t));
			if (new_list == NULL)
				return (NULL);
			new_list->n = n;
			new_list->next = next;
			new_list->prev = prev;
			if (next != NULL)
				next->prev = new_list;
			prev->next = new_list;
			break;
		}
		position++;
		cpy = cpy->next;
	}
	return (new_list);


}
