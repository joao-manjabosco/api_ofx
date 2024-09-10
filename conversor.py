from decimal import Decimal

# Função para processar os dados OFX
def process_ofx(ofx_data):
    account = ofx_data.account

    conta = [{
        'numero da conta': account.account_id,
        'numero_roteamento_banco': account.routing_number,
        'agencia': account.branch_id,
        'tipo_conta': account.type
    }]

    institution = account.institution
    instituicao = [{
        'instituicao_banco': institution.organization
    }]

    statement = account.statement
    statem = [{
        'start_date': statement.start_date.isoformat() if statement.start_date else None,
        'end_date': statement.end_date.isoformat() if statement.end_date else None,
        'balance': float(statement.balance) if isinstance(statement.balance, Decimal) else statement.balance
    }]

    transact = []
    for transaction in statement.transactions:
        transact.append({
            'payee': transaction.payee,
            'type': transaction.type,
            'date': transaction.date.isoformat() if transaction.date else None,
            'user_date': transaction.user_date.isoformat() if transaction.user_date else None,
            'amount': float(transaction.amount) if isinstance(transaction.amount, Decimal) else transaction.amount,
            'id': transaction.id,
            'memo': transaction.memo,
            'sic': transaction.sic,
            'mcc': transaction.mcc,
            'checknum': transaction.checknum
        })

    resultado = {
        'instituicao': instituicao,
        'conta': conta,
        'extrato': statem,
        'transacoes': transact
    }

    return resultado
