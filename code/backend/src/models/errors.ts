interface IRequestError {
  status: number;
  details: {
    code: string;
    message: string;
  };
}

const PF001: IRequestError = {
  status: 400,
  details: { code: "PF001", message: "Requisição inválida." },
};

const NF001: IRequestError = {
  status: 404,
  details: { code: "NF001", message: "Dados não encontrados." },
};

const IE001: IRequestError = {
  status: 500,
  details: { code: "IE001", message: "Erro interno na aplicação." },
};

export { PF001, NF001, IE001 };
