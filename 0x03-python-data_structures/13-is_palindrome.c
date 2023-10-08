#include "lists.h"

/**
 * is_palindrome - Checks if its a palindrome
 * @head: head
 * Return: 1 if true and 0 if false.
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int i, start, end, list_len;

	if (*head == NULL || temp->next == NULL)
		return (1);

	while (temp != NULL)
	{
		list_len++;
		temp = temp->next;
	}

	for (i = 0; i < (list_len / 2); i++)
	{
		start = get_value_at_index(head, i);
		end = get_value_at_index(head, list_len - 1 - i);
		if (start != end)
			return (0);
	}
	return (1);
}

/**
 * get_value_at_index - Get's value at a given index
 * @head: Head
 * @idx: index
 * Return: value at the given index
*/
int get_value_at_index(listint_t **head, int idx)
{
	listint_t *temp = *head;
	int i;

	for (i = 0; i < idx; i++)
		temp = temp->next;
	return (temp->n);
}
