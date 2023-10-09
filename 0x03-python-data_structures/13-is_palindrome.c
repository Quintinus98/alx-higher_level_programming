#include "lists.h"

/**
 * is_palindrome - Checks if its a palindrome
 * @head: head
 * Return: 1 if true and 0 if false.
*/
int is_palindrome(listint_t **head)
{
	int i, len;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	len = len_list(head);

	for (i = 0; i < (len / 2); i++)
	{
		if (get_val(head, i) != get_val(head, len - 1 - i))
			return (0);
	}
	return (1);
}

/**
 * get_val - Get's value at a given index
 * @head: Head
 * @idx: index
 * Return: value at the given index
*/
int get_val(listint_t **head, int idx)
{
	listint_t *temp = *head;
	int i;

	for (i = 0; i < idx; i++)
		temp = temp->next;
	return (temp->n);
}

/**
 * len_list - Length of linked list
 * @head: Linked list
 * Return: Length of linked list
*/
int len_list(listint_t **head)
{
	listint_t *temp = *head;
	int cnt = 0;

	if (*head == NULL)
		return (0);
	while (temp != NULL)
	{
		cnt++;
		temp = temp->next;
	}
	return (cnt);
}
