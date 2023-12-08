#include "lists.h"

/**
 * add_dnodeint - Adds a new node at the beginning of a dlistint_t list.
 * @head: Pointer to the address of the head of the list.
 * @n: Value to be assigned to the new node.
 *
 * Return: Address of the new node, or NULL if it fails.
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_list = malloc(sizeof(dlistint_t));
	if (new_list == NULL)
		return (NULL);

	new_list->n = n;
	new_list->next = *head;
	new_list->prev = NULL;
	*head = new_list;
	 return (new_list);
}
