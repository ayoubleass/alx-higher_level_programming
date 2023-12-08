#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes the node at a given
 * position in a dlistint_t list.
 * @head: Pointer to the address of the head of the list.
 * @index: Index of the node to be deleted.
 *
 * Return: 1 if successful, -1 if the node does not exist or deletion fails.
 */

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *next, *prev, *target;
	unsigned int position = 0;
	dlistint_t *copy = *head;

	if (*head == NULL)
		return (-1);

	if (index == 0)
	{
		target = *head;
		*head = target->next;
		if (*head != NULL)
			(*head)->prev = NULL;
		free(target);
		return (1);
	}

	while (copy != NULL)
	{
		if (position  == index - 1)
		{
			prev = copy;
		}
		if (position == index)
		{
			next = copy->next;
			free(copy);
			if (next != NULL)
				next->prev = prev;
			prev->next = next;
			return (1);
		}
		position++;
		copy = copy->next;
	}
	return (-1);

}
