#include "lists.h"

/**
 * reverse - Reverses a linked list.
 * @head: Pointer to the head of the list.
 *
 * Return: Pointer to the head of the reversed list.
 */
listint_t *reverse(listint_t *head)
{
	listint_t *new_list;
	listint_t *h;

	h = NULL;
	if (head == NULL)
		return (NULL);
	while (head != NULL)
	{
		new_list = malloc(sizeof(listint_t));
		if (new_list == NULL)
			return (NULL);
		new_list->n = head->n;
		new_list->next = h;
		h = new_list;
		head = head->next;
	}
	return (new_list);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *new_list = NULL;

	new_list = reverse(*head);
	if (new_list == NULL)
		return  (0);

	while (new_list != NULL && *head != NULL)
	{
		if (new_list->n != (*head)->n)
		{
			free_listint(new_list);
			return (0);
		}
		new_list = new_list->next;
		*head = (*head)->next;
	}
	free_listint(new_list);
	return (1);
}
