#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node to a sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *newNode = malloc(sizeof(listint_t));
	int idx = 0;

	if (!newNode || !temp)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	while (temp->n < newNode->n)
	{
		if (!temp->next)
			return (NULL);
		temp = temp->next;
		idx++;
	}
	temp = *head;
	while (idx != 1)
	{
		temp = temp->next;
		idx--;
	}

	newNode->next = temp->next;
	temp->next = newNode;
	return (newNode);
}
