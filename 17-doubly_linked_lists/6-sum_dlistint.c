#include "lists.h"

/**
 * sum_dlistint - Calculates the sum of all the elements in a dlistint_t list.
 * @head: Pointer to the head of the list.
 *
 * Return: Sum of all elements, or 0 if the list is empty.
 */

int sum_dlistint(dlistint_t *head)
{
	int sum = 0;

	while (head != NULL)
	{
		sum = sum + head->n;
		head = head->next;
	}
	return (sum);
}
