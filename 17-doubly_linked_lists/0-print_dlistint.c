#include "lists.h"



/**
 * print_dlistint - Prints all the elements of a dlistint_t list.
 * @h: Pointer to the head of the list.
 *
 * Return: The number of nodes.
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t list_len = 0;
	const dlistint_t *cpy = NULL;

	cpy = h;
	while (cpy != NULL)
	{
		printf("%d\n", cpy->n);
		list_len++;
		cpy = cpy->next;
	}
	return (list_len);
}
